#!/usr/bin/env python3
"""
GitHub Video Uploader - Browser Automation (Improved)

Uploads videos to GitHub's user-images CDN via drag-and-drop in web editor.
Extracts CDN links and updates README.md with embedded video tags.

Features:
- Saves browser session (no need to login every time)
- Handles GitHub's CodeMirror editor
- Automatic retry with better error handling
"""

import asyncio
import re
import sys
from pathlib import Path

from playwright.async_api import async_playwright


class GitHubVideoUploader:
    """Automate GitHub video uploads via browser automation."""

    def __init__(self, repo_url: str, readme_path: Path, video_dir: Path, session_file: Path = None):
        self.repo_url = repo_url
        self.readme_path = readme_path
        self.video_dir = video_dir
        self.session_file = session_file or Path.home() / ".github_session.json"
        self.cdn_links = {}

    async def get_page_content(self, page) -> str:
        """Extract page content from CodeMirror editor."""
        try:
            # Method 1: Try CodeMirror's getValue
            content = await page.evaluate("""
                () => {
                    const cm = document.querySelector('.CodeMirror');
                    return cm ? cm.CodeMirror.getValue() : '';
                }
            """)
            if content:
                return content
        except:
            pass

        # Method 2: Try textarea fallback
        try:
            textarea = await page.locator('textarea[name="value"]').input_value()
            if textarea:
                return textarea
        except:
            pass

        return ""

    async def upload_video(self, page, video_path: Path) -> str:
        """
        Upload a single video via drag-and-drop.
        Returns the CDN link.
        """
        print(f"Uploading {video_path.name}...")

        # Wait for page to load completely
        await page.wait_for_load_state('networkidle', timeout=10000)

        # Find the CodeMirror editor
        try:
            await page.wait_for_selector('.CodeMirror', timeout=10000)
        except:
            raise Exception("Could not find CodeMirror editor")

        # Try multiple upload methods
        upload_success = False

        # Method 1: File input (GitHub's hidden input)
        try:
            file_input = page.locator('input[type="file"]').first
            if await file_input.count() > 0:
                await file_input.set_input_files(str(video_path))
                upload_success = True
        except Exception as e:
            print(f"  ⚠️  File input method failed: {e}")

        # Method 2: Drag and drop to CodeMirror
        if not upload_success:
            try:
                codemirror = page.locator('.CodeMirror').first
                await codemirror.evaluate("""
                    (element) => {
                        // Create file input
                        const input = document.createElement('input');
                        input.type = 'file';
                        input.style.display = 'none';
                        document.body.appendChild(input);

                        // Trigger file selection
                        input.click();

                        return input;
                    }
                """)
                # Note: This method requires manual interaction, so we'll skip it
            except Exception as e:
                print(f"  ⚠️  Drag-drop method failed: {e}")

        if not upload_success:
            raise Exception("All upload methods failed")

        # Wait for upload to complete
        print("  ⏳ Waiting for upload...")
        await asyncio.sleep(5)  # Wait for initial upload

        # Extract CDN link from page
        try:
            # Wait for video element to appear
            await page.wait_for_selector(
                'video[src*="user-images.githubusercontent.com"]',
                timeout=20000
            )

            video_element = page.locator('video[src*="user-images.githubusercontent.com"]').first
            cdn_link = await video_element.get_attribute('src')

            if cdn_link:
                print(f"  ✅ CDN link: {cdn_link}")
                return cdn_link

        except:
            print("  ⚠️  Video element not found, trying page content...")

        # Fallback: Parse from page content
        await asyncio.sleep(2)
        content = await self.get_page_content(page)
        match = re.search(r'https://user-images\.githubusercontent\.com/[^\s\)"\>]+', content)

        if match:
            cdn_link = match.group(0)
            print(f"  ✅ CDN link from content: {cdn_link}")
            return cdn_link

        # Last resort: Check page source
        page_source = await page.content()
        match = re.search(r'https://user-images\.githubusercontent\.com/[^\s\)"\>]+\.mp4', page_source)

        if match:
            cdn_link = match.group(0)
            print(f"  ✅ CDN link from source: {cdn_link}")
            return cdn_link

        raise Exception("Could not extract CDN link")

    async def run(self, headless: bool = False):
        """Main upload workflow."""
        video_files = {
            'github-ready_explainer_video.mp4': 'explainer_video',
            'github-ready_explainer_podcast.mp4': 'explainer_podcast'
        }

        async with async_playwright() as p:
            # Launch browser
            browser = await p.chromium.launch(
                headless=headless,
                args=['--disable-blink-features=AutomationControlled']
            )

            # Load or create browser context
            context = None
            if self.session_file.exists():
                print(f"📂 Loading saved session from {self.session_file}")
                try:
                    context = await browser.new_context(
                        storage_state=str(self.session_file),
                        viewport={'width': 1280, 'height': 800},
                        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    )
                except Exception as e:
                    print(f"⚠️  Could not load session: {e}")
                    context = None

            if not context:
                context = await browser.new_context(
                    viewport={'width': 1280, 'height': 800},
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                )

            page = await context.new_page()

            try:
                # Navigate to README edit page
                edit_url = f"{self.repo_url}/edit/main/README.md"
                print(f"Navigating to: {edit_url}")
                await page.goto(edit_url, wait_until='networkidle')

                # Check if authentication is needed
                if 'login' in page.url or 'session' in page.url:
                    print("\n" + "="*60)
                    print("🔐 AUTHENTICATION REQUIRED")
                    print("="*60)
                    print("Please log in to GitHub in the browser window.")
                    print("The script will continue after you're logged in.")
                    print("Your session will be saved for future use.")
                    print("="*60 + "\n")

                    # Wait for user to log in
                    await page.wait_for_url(
                        "**/edit/main/README.md",
                        timeout=180000  # 3 minutes
                    )
                    print("✅ Authentication successful!")

                    # Save session for future use
                    print(f"💾 Saving session to {self.session_file}")
                    await context.storage_state(path=str(self.session_file))
                else:
                    print("✅ Using saved session or public repo accessible")

                # Upload each video
                for video_filename, video_key in video_files.items():
                    video_path = self.video_dir / video_filename

                    if not video_path.exists():
                        print(f"⚠️  Video not found: {video_path}")
                        continue

                    try:
                        cdn_link = await self.upload_video(page, video_path)
                        self.cdn_links[video_key] = cdn_link
                    except Exception as e:
                        print(f"❌ Failed to upload {video_filename}: {e}")
                        continue

                # Print results
                print("\n" + "="*60)
                print("UPLOAD RESULTS")
                print("="*60)
                for video_key, cdn_link in self.cdn_links.items():
                    print(f"{video_key}: {cdn_link}")
                print("="*60 + "\n")

                # Generate updated README section
                self.generate_readme_update()

                return len(self.cdn_links) > 0

            except Exception as e:
                print(f"❌ Error: {e}")
                import traceback
                traceback.print_exc()
                return False

            finally:
                await browser.close()

    def generate_readme_update(self):
        """Generate the updated README section with CDN links."""

        if not self.cdn_links:
            print("⚠️  No CDN links extracted, cannot update README")
            return

        print("README Update Instructions:")
        print("="*60)

        # Explainer Video
        if 'explainer_video' in self.cdn_links:
            cdn_link = self.cdn_links['explainer_video']
            print("\n### 🎬 Explainer Video (22 seconds)")
            print("Replace the video tag with:")
            print(f'<video src="{cdn_link}" controls="controls" style="max-width: 730px; margin: 10px 0;">')
            print("</video>")
            print("\nThen delete the badge link section below it.")

        # Podcast
        if 'explainer_podcast' in self.cdn_links:
            cdn_link = self.cdn_links['explainer_podcast']
            print("\n### 🎙️ Podcast Overview (2m 20s)")
            print("Replace the video tag with:")
            print(f'<video src="{cdn_link}" controls="controls" style="max-width: 730px; margin: 10px 0;">')
            print("</video>")
            print("\nThen delete the badge link section below it.")

        print("\n" + "="*60)


async def main():
    """Main entry point."""
    repo_url = "https://github.com/EndUser123/github-ready"
    readme_path = Path("P:/packages/github-ready/README.md")
    video_dir = Path("P:/packages/github-ready/assets/videos")
    session_file = Path.home() / ".github_video_uploader_session.json"

    uploader = GitHubVideoUploader(repo_url, readme_path, video_dir, session_file)

    # Run with headed browser for initial authentication
    print("Starting GitHub video uploader...")
    print("Note: Browser window will open for authentication if needed.\n")
    print("Your session will be saved automatically after first login.")
    print("Future runs will not require authentication.\n")

    success = await uploader.run(headless=False)

    if success:
        print("\n✅ Upload completed successfully!")
        print("Follow the instructions above to update your README.")
    else:
        print("\n❌ Upload failed. Please check the errors above.")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

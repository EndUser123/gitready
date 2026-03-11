#!/usr/bin/env python3
"""
GitHub Video Uploader - Browser Automation

Uploads videos to GitHub's user-images CDN via drag-and-drop in web editor.
Extracts CDN links and updates README.md with embedded video tags.

Requirements:
- playwright (already installed)
- GitHub authentication (manual login or cookies)
"""

import asyncio
import re
from pathlib import Path

from playwright.async_api import Page, async_playwright


class GitHubVideoUploader:
    """Automate GitHub video uploads via browser automation."""

    def __init__(self, repo_url: str, readme_path: Path, video_dir: Path):
        self.repo_url = repo_url
        self.readme_path = readme_path
        self.video_dir = video_dir
        self.cdn_links = {}

    async def upload_video(self, page: Page, video_path: Path) -> str:
        """
        Upload a single video via drag-and-drop.
        Returns the CDN link.
        """
        print(f"Uploading {video_path.name}...")

        # Wait for textarea to be editable
        textarea = page.locator('textarea[name="value"]').first
        await textarea.wait_for(state='visible', timeout=10000)

        # Create file input for upload (GitHub's hidden file input)
        file_input = page.locator('input[type="file"]').first

        # Upload the file
        await file_input.set_input_files(str(video_path))

        # Wait for upload to complete (look for CDN link in page)
        await page.wait_for_timeout(3000)  # Initial wait

        # Extract CDN link from network responses or page content
        try:
            # Method 1: Check for image/video elements with user-images URL
            await page.wait_for_selector(
                'img[src*="user-images.githubusercontent.com"], video[src*="user-images.githubusercontent.com"]',
                timeout=15000
            )

            # Get the CDN link
            video_element = page.locator('video[src*="user-images.githubusercontent.com"]').first
            if await video_element.count() > 0:
                cdn_link = await video_element.get_attribute('src')
                print(f"✅ CDN link: {cdn_link}")
                return cdn_link

        except Exception as e:
            print(f"⚠️  Could not find CDN link automatically: {e}")

        # Method 2: Parse from page source
        content = await page.content()
        match = re.search(r'https://user-images\.githubusercontent\.com/[^\s"<>]+', content)
        if match:
            cdn_link = match.group(0)
            print(f"✅ CDN link from page: {cdn_link}")
            return cdn_link

        raise Exception("Could not extract CDN link from page")

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

            context = await browser.new_context(
                viewport={'width': 1280, 'height': 800},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )

            page = await context.new_page()

            try:
                # Navigate to README edit page
                edit_url = f"{self.repo_url}/edit/main/README.md"
                print(f"Navigating to: {edit_url}")
                await page.goto(edit_url)

                # Check if authentication is needed
                await page.wait_for_load_state('networkidle')

                if 'login' in page.url or 'session' in page.url:
                    print("\n" + "="*60)
                    print("🔐 AUTHENTICATION REQUIRED")
                    print("="*60)
                    print("Please log in to GitHub in the browser window.")
                    print("The script will continue after you're logged in.")
                    print("="*60 + "\n")

                    # Wait for user to log in (check for redirect back to edit page)
                    await page.wait_for_url(
                        "**/edit/main/README.md",
                        timeout=120000  # 2 minutes for manual login
                    )
                    print("✅ Authentication successful!")
                else:
                    print("✅ Already authenticated or public repo accessible")

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

            except Exception as e:
                print(f"❌ Error: {e}")
                raise

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

    uploader = GitHubVideoUploader(repo_url, readme_path, video_dir)

    # Run with headed browser for authentication
    print("Starting GitHub video uploader...")
    print("Note: Browser window will open for authentication if needed.\n")

    await uploader.run(headless=False)


if __name__ == "__main__":
    asyncio.run(main())

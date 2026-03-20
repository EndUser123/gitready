# github-ready

[![Version](https://img.shields.io/badge/version-5.15.2-blue.svg)](https://github.com/EndUser123/github-ready)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-purple.svg)](https://github.com/EndUser123/github-ready)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/EndUser123/github-ready/actions)

> Universal Package Creator and Portfolio Polisher v5.15.2

Create GitHub-ready Python libraries, Claude skills, and Claude Code plugins with badges, CI/CD workflows, coverage metrics, media artifacts, and automated GitHub publication.

## Quick Start

```bash
# Create a new package (auto-detects type)
/github-ready mylib

# Polish existing repository
/github-ready --target P:/packages/existing-repo

# Preview what will happen
/github-ready --dry-run myproject
```

## Explainer Video

[![Watch the demo with audio](assets/videos/debug_screenshot.png)](https://enduser123.github.io/github-ready/docs/video.html)

> **[🎬 Watch the explainer in the browser](https://enduser123.github.io/github-ready/docs/video.html)**
> **[⬇️ Download the MP4 directly](https://github.com/EndUser123/github-ready/releases/download/media/github_ready_explainer_pbs.mp4)**
> *Browser playback requires GitHub Pages to be enabled for this repository.*

**Quick overview**: Features, workflow, and automated portfolio polish.
*Runtime should match the exported NotebookLM asset; update this text only after verifying the final file duration.*

## What github-ready Does

- 🎯 **Intelligent Detection**: Automatically detects package type and requirements from project structure
- 📦 **Multi-Format Support**: Creates Claude skills, Python libraries, and Claude Code plugins
- 🎨 **Portfolio Polish**: Adds badges, CI/CD, CHANGELOG, API docs, and media artifacts
- 🎬 **Media Generation**: Creates banners, diagrams, explainer videos, and presentations
- 🔍 **Code Review**: Automated quality validation before portfolio polish
- 🔄 **Brownfield Conversion**: Converts existing Python libraries to plugins
- 🚀 **GitHub Publication**: Automated monorepo extraction and repository creation

**One command → Full intelligent pipeline:**

1. **DETECT** — Scan repository, identify gaps and needs
2. **ANALYZE** — Determine package type automatically
3. **GENERATE** — Create all missing artifacts (structure, badges, CI/CD, docs, CHANGELOG)
4. **VALIDATE** — Verify everything works
5. **CLEANUP** — Detect and remove obsolete files from refactoring
6. **PUBLISH** — Extract from monorepo, create GitHub repository, push code
7. **REPORT** — Show what was created with evidence

## PHASE 6: GitHub Publication

**PHASE 6** provides end-to-end GitHub repository creation and publishing automation. This is useful for packages developed in a monorepo that need to be published as standalone repositories.

### Prerequisites

- **git 2.30+** for subtree split support
- **GitHub CLI (gh)** for automated repository creation (optional but recommended)
- **GitHub account** with appropriate permissions

### Scripts

Two Python scripts are provided for Windows-compatible GitHub publication:

#### `extract_from_monorepo.py`

Extracts a package from a monorepo with two methods:

1. **Subtree Split** (default): Preserves git history from the monorepo using `git subtree split`
2. **Fresh Init** (`--fresh-init`): Creates a clean git history without monorepo artifacts

```bash
# Extract with history preservation (default)
python scripts/extract_from_monorepo.py P:/packages/my-package my-package

# Extract with fresh git history
python scripts/extract_from_monorepo.py P:/packages/my-package my-package --fresh-init
```

#### `create_github_repo.py`

Creates a GitHub repository and pushes the extracted code:

```bash
# Create repository with description
python scripts/create_github_repo.py "my-package" "P:/packages/my-package" "My awesome library"
```

### Publication Workflow

1. **Extraction**: Run `extract_from_monorepo.py` to extract the package from the monorepo
2. **Repository Creation**: Run `create_github_repo.py` to create the GitHub repository
3. **Verification**: The script verifies the repository was created successfully

### Manual Fallback

If GitHub CLI is not available, `create_github_repo.py` provides manual instructions with curl API commands and GitHub web interface steps.

## PHASE 7: Repository Finalization

**PHASE 7** automates post-publish tasks that should happen immediately after repo creation. This includes GitHub Pages enablement, initial release creation, repository topics, and governance files.

### Prerequisites

- **GitHub CLI (gh)** for automated repository operations
- **GitHub account** with appropriate permissions

### Script: `finalize_github_repo.py`

Automates the following tasks:

1. **GitHub Pages Enablement**
   - Automatically enables GitHub Pages for documentation
   - Sets correct branch/directory (root or /docs)
   - Provides Pages URL for verification

2. **Initial Release Creation**
   - Creates v0.1.0 or v1.0.0 release via `gh release create`
   - Generates release notes from CHANGELOG.md
   - Provides release URL for verification

3. **Repository Topics/Tags**
   - Adds relevant topics based on package type (python, claude-code, plugin, mcp, etc.)
   - Improves repository discoverability

4. **CODEOWNERS File**
   - Generates CODEOWNERS file from git config or provided username
   - Essential for collaborative projects

5. **SECURITY.md File**
   - Generates security policy template
   - Includes vulnerability reporting instructions

```bash
# Finalize after GitHub publication
python scripts/finalize_github_repo.py my-package P:/packages/my-package --package-type plugin

# With options
python scripts/finalize_github_repo.py my-package . --release-version 1.0.0 --username myuser

# Skip specific steps
python scripts/finalize_github_repo.py my-package . --skip-pages --skip-release

# Verify finalization status
python scripts/finalize_github_repo.py my-package . --verify
```

### Options

- `--package-type` - Type of package (plugin, skill, mcp, library, tool)
- `--release-version` - Version for initial release (default: 0.1.0)
- `--username` - GitHub username for CODEOWNERS
- `--skip-pages` - Skip GitHub Pages enablement
- `--skip-release` - Skip initial release creation
- `--skip-topics` - Skip adding repository topics
- `--skip-codeowners` - Skip CODEOWNERS file generation
- `--skip-security` - Skip SECURITY.md generation
- `--verify` - Verify finalization status and exit

### Output

Fully finalized GitHub repository with:
- GitHub Pages enabled and URL provided
- Initial release created with notes from CHANGELOG
- Repository topics added for discoverability
- CODEOWNERS file for collaboration
- SECURITY.md file for vulnerability reporting

## PHASE 4.5: Quality Scanning

**PHASE 4.5** provides automated security and dependency scanning during the validation phase. This helps identify potential issues before publishing.

### Prerequisites

- **bandit** for Python security linting (`pip install bandit`)
- **safety** for known vulnerability checks (`pip install safety`)
- **pip-audit** for dependency auditing (`pip install pip-audit`)

### Script: `scan_package_quality.py`

Performs the following checks:

1. **Security Scanning**
   - Runs `bandit` for Python security issues
   - Runs `safety` for known vulnerable dependencies
   - Reports issues by severity (HIGH, MEDIUM, LOW)

2. **Dependency Auditing**
   - Runs `pip-audit` for vulnerability scanning
   - Checks for outdated packages
   - Reports affected versions

3. **Badge Validation**
   - Verifies all badge URLs in README.md are reachable
   - Checks CI/CD badges reference correct workflows
   - Warns about broken badges

4. **Quality Metrics**
   - Counts Python files and test files
   - Calculates test ratio
   - Reports total lines of code

```bash
# Scan package quality
python scripts/scan_package_quality.py P:/packages/my-package

# Save report to file
python scripts/scan_package_quality.py . --save-report

# Skip specific checks
python scripts/scan_package_quality.py . --skip-badges --skip-quality

# Exit with error if issues found
python scripts/scan_package_quality.py . --fail-on-issues
```

### Options

- `--skip-security` - Skip security scanning (bandit, safety)
- `--skip-audit` - Skip dependency auditing (pip-audit)
- `--skip-badges` - Skip badge validation
- `--skip-quality` - Skip code quality metrics
- `--save-report` - Save scan results to .quality-report.json
- `--fail-on-issues` - Exit with error code if issues are found

### Output

Quality scan report with:
- Security issues found (if any)
- Known vulnerabilities in dependencies
- Broken or missing badge references
- Code quality metrics (file counts, test ratio, LOC)
- Overall assessment and recommendations

## Development and Deployment

## Development and Deployment

### Three Deployment Models

**IMPORTANT**: This package supports three different deployment modes. Choose the right one for your use case.

#### 1. SKILLS (Dev Deployment) ⭐ **Recommended for Development**

**For**: When you're actively developing this package and want instant feedback.

**Setup:**
```powershell
# Windows (Junction - No admin required)
# For plugins with skills: Junction to the skills/ subdirectory
New-Item -ItemType Junction -Path "P:\.claude\skills\package" -Target "P:\packages\github-ready\skills\github-ready"

# macOS/Linux (Symlink)
ln -s /path/to/packages/github-ready/skills/github-ready ~/.claude/skills/package
```

**Key points:**
- ✅ Edit in `P:/packages/github-ready`, changes work immediately
- ✅ No reinstallation required - skills auto-discover from `P:/.claude/skills/`
- ✅ Perfect for active development
- ✅ Junction to `skills/github-ready/` subdirectory (where SKILL.md actually lives)
- ⚠️  **CRITICAL**: The junction target points to WHERE THE SKILL.md FILE ACTUALLY LIVES
  - Plugin skills: `package-name/skills/skill-name/SKILL.md` → junction target: `skills/skill-name/`

#### 2. HOOKS (Dev Deployment - Hook Files Only)

**For**: When this package has hook files (`.py` files in `core/hooks/`) you want to test.

**Setup:**
```powershell
# Symlink individual hook files to P:/.claude/hooks/
cd P:/.claude/hooks

# Example: Symlink a specific hook file
cmd /c "mklink HookName.py P:/packages/github-ready/core/hooks/HookName.py"
```

**Key points:**
- ✅ Symlink individual `.py` hook files only (NOT the entire directory)
- ✅ Symlinks go in `P:/.claude/hooks/` (NOT `~/.claude/plugins/`)
- ✅ These are dev-only symlinks for working directly on source code
- ⚠️  After brownfield conversion, check for broken symlinks pointing to old `src/` paths

#### 3. PLUGINS (End User Deployment)

**For**: Distributing this package to other users via marketplace or GitHub.

**Setup:**
```bash
# End users install via /plugin command
/plugin P:/packages/github-ready

# Or from marketplace (when published)
/plugin install github-ready
```

**Key points:**
- ✅ Plugin copied to `~/.claude/plugins/cache/`
- ✅ Registered in `~/.claude/plugins/installed_plugins.json`
- ❌ **NOT for local development** - requires reinstall on every change
- ✅ Use for distributing finished packages to users

### Which Model Should You Use?

| Your Situation | Use This Model | Why |
|----------------|----------------|-----|
| Actively developing this package | **SKILLS** (junction) | Instant feedback, no reinstall |
| Testing hook file changes | **HOOKS** (symlinks) | Direct hook testing |
| Distributing to end users | **PLUGINS** (/plugin) | Proper distribution format |

### Common Mistakes to Avoid

- ❌ Don't use `/plugin` command for local development (requires reinstall on every change)
- ❌ Don't symlink entire directories to `P:/.claude/hooks/` (only symlink `.py` files)
- ❌ Don't confuse skills (`P:/.claude/skills/`) with plugins (`~/.claude/plugins/`)
- ❌ Don't forget to update symlinks after brownfield conversion - check for `src/` paths

## Additional Media Assets

> 💡 **Note**: These assets were generated using NotebookLM integration and automatically published to GitHub Releases for easy access.

### 📊 Architecture Flowchart

```mermaid
graph TB
    Input[User: /github-ready mylib] --> Detect[Detect Package Type]

    Detect --> Type{Package Type?}

    Type -->|Claude Code Plugin| Plugin[Plugin Structure]
    Type -->|Claude Skill| Skill[Skill Structure]
    Type -->|Python Library| Library[Library Structure]

    Plugin --> Scaffold[Scaffolding and Generation]
    Skill --> Scaffold
    Library --> Scaffold

    Scaffold --> Polish[Portfolio Polish]

    Polish --> Badges[Badges and Metrics]
    Polish --> CI[CI/CD Workflows]
    Polish --> Docs[Documentation]
    Polish --> Media[Media Assets]

    Media --> Diagram[Architecture Flowchart]
    Media --> Video[Explainer Videos]
    Media --> Slides[Presentation Slides]

    Badges --> Quality[Quality Validation]
    CI --> Quality
    Docs --> Quality

    Quality --> Output[GitHub-Ready Package]

    style Input fill:#1f6feb
    style Output fill:#238636
    style Detect fill:#21262d
    style Scaffold fill:#21262d
    style Polish fill:#21262d
    style Quality fill:#21262d
```

### 📑 Presentation Slides

[![Slide deck preview](assets/slides/github_ready_slides_preview.png)](assets/slides/github_ready_slides.pdf)

**[📄 View Slides (PDF)](assets/slides/github_ready_slides.pdf)**
**[⬇️ Download PDF](assets/slides/github_ready_slides.pdf)**

*Use the PDF for both viewing and download on GitHub.*

---

**💡 Tip**: Keep the slide deck in PDF form for the cleanest GitHub viewing experience.

## Package Types

| Type | Trigger | Structure | Use Case |
|------|---------|-----------|----------|
| **Claude Code Plugin** | `.claude-plugin/` directory | `.claude-plugin/` + `core/` + `hooks/` | **DEFAULT**: Packages with hooks/skills |
| **Claude Plugin + MCP** | `.claude-plugin/` + MCP server | Adds `.mcp.json` | Plugins with MCP server |
| **Brownfield Plugin** | Python library + conversion | `src/` → `core/` migration | Convert existing Python lib |
| **Python Library** | `src/` or `pyproject.toml` | `src/{{NAME}}/` + `tests/` | Pure backend code (no hooks) |
| **Claude Skill** | `SKILL.md` exists | `skill/` only | Standalone Claude skills |

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Resources

- [templates/](templates/) - Template files for various package elements
- [Video Workflow Template](templates/video-section-template.md) - Copy-paste template for README videos
- [scripts/extract_from_monorepo.py](scripts/extract_from_monorepo.py) - Extract package from monorepo for GitHub publication
- [scripts/create_github_repo.py](scripts/create_github_repo.py) - Create GitHub repository and push code

---

**github-ready** - Create portfolio-worthy Python packages, skills, and plugins

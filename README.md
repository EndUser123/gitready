# github-ready

[![Version](https://img.shields.io/badge/version-5.5.0-blue.svg)](https://github.com/EndUser123/github-ready)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-purple.svg)](https://github.com/EndUser123/github-ready)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/EndUser123/github-ready/actions)

> Universal Package Creator & Portfolio Polisher v5.5.0

Create GitHub-ready Python libraries, Claude skills, and Claude Code plugins with badges, CI/CD workflows, coverage metrics, and media artifacts.

## Installation

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

## Features

- 🎯 **Intelligent Detection**: Automatically detects package type and requirements from project structure
- 📦 **Multi-Format Support**: Creates Claude skills, Python libraries, and Claude Code plugins
- 🎨 **Portfolio Polish**: Adds badges, CI/CD, CHANGELOG, API docs, and media artifacts
- 🎬 **Media Generation**: Creates banners, diagrams, explainer videos, and presentations
- 🔍 **Code Review**: Automated quality validation before portfolio polish
- 🔄 **Brownfield Conversion**: Converts existing Python libraries to plugins

## Quick Start

```bash
# Create a new package (auto-detects type)
/github-ready mylib

# Polish existing repository
/github-ready --target P:/packages/existing-repo

# Preview what will happen
/github-ready --dry-run myproject
```

## What It Does

**One command → Full intelligent pipeline:**

1. **DETECT** — Scan repository, identify gaps and needs
2. **ANALYZE** — Determine package type automatically
3. **GENERATE** — Create all missing artifacts (structure, badges, CI/CD, docs, CHANGELOG)
4. **VALIDATE** — Verify everything works
5. **CLEANUP** — Detect and remove obsolete files from refactoring
6. **REPORT** — Show what was created with evidence

## Media Assets

> 💡 **Note**: These assets were generated using NotebookLM integration and automatically published to GitHub Releases for easy access.

### 🎙️ Explainer Video (22 seconds)

[![Watch the demo with audio](assets/preview.gif)](https://github.com/EndUser123/github-ready/releases/download/media/github_ready_explainer_pbs.mp4)

> **[🎬 Click here to watch the full Explainer Video with Audio](https://github.com/EndUser123/github-ready/releases/download/media/github_ready_explainer_pbs.mp4)**
> *Generated by NotebookLM - featuring full technical narration and architecture walkthrough (33MB)*

**Quick overview**: Features, workflow, and automated portfolio polish

---

### 📊 Architecture Diagrams

#### Complete Workflow

```mermaid
graph TB
    Start([User: /package mylib]) --> Prep[Phase 1: Diagnose & Prep]
    Prep --> Detect[Phase 1.5: Detect Package Type]

    Detect --> Type{Package Type?}

    Type -->|Claude Code Plugin| Plugin1[.claude-plugin/]
    Type -->|Claude Skill| Skill1[skill/]
    Type -->|Python Library| Lib1[src/]

    Plugin1 --> Build[Phase 2: Build Structure]
    Skill1 --> Build
    Lib1 --> Build

    Build --> Templates[Phase 3: Generate Templates]
    Templates --> Validate[Phase 4: Validate]

    Validate --> CodeReview[Phase 4.5: Code Review]
    CodeReview --> Media[Phase 4.7: Media Generation]

    Media --> NotebookLM[NotebookLM Assets]
    Media --> Mermaid[C4 Diagrams]
    Media --> HTML[Interactive HTML]
    Media --> OpenRouter[Optional Banner]

    NotebookLM --> Polish[Phase 5: Portfolio Polish]
    Mermaid --> Polish
    HTML --> Polish
    OpenRouter --> Polish

    Polish --> Badges[Badges & CI/CD]
    Polish --> Docs[Documentation]
    Polish --> Changelog[CHANGELOG.md]

    Badges --> Clean[Phase 6: Cleanup]
    Docs --> Clean
    Changelog --> Clean

    Clean --> Git[Phase 7: Git Ready]
    Git --> Complete([GitHub-Ready Package])

    style Start fill:#7c3aed
    style Complete fill:#10b981
    style Detect fill:#3b82f6
    style Build fill:#3b82f6
    style Validate fill:#3b82f6
    style CodeReview fill:#f59e0b
    style Media fill:#ec4899
    style Polish fill:#8b5cf6
    style Clean fill:#6b7280
```

#### Static Diagrams

![Architecture Diagram](assets/infographics/github-ready_architecture.png)
*High-level system overview generated by NotebookLM*

#### Interactive HTML Diagrams

**[🎨 Interactive Architecture Overview →](docs/github-ready-architecture.html)**
*Explore system components and data flow with pan & zoom*

**[🎨 Interactive Workflow Diagram →](docs/github-ready-workflow.html)**
*Enhanced interactive version with detailed phase breakdown*

---

### 📑 Presentation Slides

**[📄 View PDF in GitHub viewer](assets/slides/github-ready_slides.pdf)** | [📥 Download PDF](assets/slides/github-ready_slides.pdf) | [📊 Download PPTX (editable)](assets/slides/github-ready_slides.pptx)

---

### 🎨 Infographic

![Architecture Infographic](assets/infographics/github_ready_notebooklm.png)

*Visual overview of the github-ready system architecture*

**[⬇️ Download PNG](assets/infographics/github_ready_notebooklm.png)**

---

### 📐 System Architecture (C4 Diagrams)

#### System Context

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1f6feb', 'primaryTextColor': '#c9d1d9', 'primaryBorderColor': '#58a6ff', 'lineColor': '#58a6ff', 'secondaryColor': '#21262d', 'tertiaryColor': '#161b22'}}}%%

C4Context
    title System Context - github-ready Package Creator

    Person(user, "Package Developer", "Creates packages using /github-ready command")

    System(github_ready, "github-ready", "Universal Package Creator & Portfolio Polisher")

    System_Bnd(gitHub, "GitHub", "Code hosting and collaboration platform")

    System_Bnd(notebookLM, "NotebookLM", "AI-powered research and note-taking", "Optional")

    Rel(user, github_ready, "Uses", "CLI command (/github-ready)")
    Rel(github_ready, gitHub, "Publishes", "Portfolio-ready packages")
    Rel(github_ready, notebookLM, "Generates", "Media assets (optional)")

    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="2")
```

#### Container Diagram

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1f6feb', 'primaryTextColor': '#c9d1d9', 'primaryBorderColor': '#58a6ff', 'lineColor': '#58a6ff', 'secondaryColor': '#21262d', 'tertiaryColor': '#161b22'}}}%%

C4Container
    title Container Diagram - github-ready Architecture

    Person(user, "Package Developer", "Creates packages")

    Container_Bnd(cli, "CLI Interface", "Claude Code", "/github-ready command", "Skill invocation")

    Container(skill, "Package Skill", "Python", "Main package creation logic", "Core processing")

    Container_Ext(notebookLM, "NotebookLM", "External Service", "AI media generation", "Optional integration")

    ContainerDb(localFiles, "Package Files", "File System", "Source code, configs, docs")

    Rel(user, cli, "Invokes")
    Rel(cli, skill, "Executes")
    Rel(skill, localFiles, "Reads", "Package structure")
    Rel(skill, localFiles, "Writes", "Generated artifacts")
    Rel(skill, notebookLM, "Uploads sources", "For media generation")
    Rel(notebookLM, skill, "Returns", "Generated assets")

    UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="2")
```

*Editable source files:* [c4_context.mmd](docs/diagrams/c4_context.mmd) | [c4_containers.mmd](docs/diagrams/c4_containers.mmd) | [c4_components.mmd](docs/diagrams/c4_components.mmd)

---

**💡 Tip**: PDFs open in GitHub's viewer with annotation support. PPTX files are editable for customizations.

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

- [NotebookLM Video Workflow](NOTEBOOKLM_VIDEO_WORKFLOW.md) - Guide for creating explainer videos
- [templates/](templates/) - Template files for various package elements
- [Video Workflow Template](templates/video-section-template.md) - Copy-paste template for README videos

---

**github-ready** - Create portfolio-worthy Python packages, skills, and plugins

---
name: github-ready
version: 5.6.0
description: This skill should be used when the user asks to "create a package", "scaffold a Python library", "make a GitHub-ready repo", "generate badges", "set up CI/CD", "convert to plugin", "brownfield conversion", "validate plugin standards", or mentions package scaffolding, portfolio polish, repository structure setup, badge generation, or plugin standards validation. Creates GitHub-ready Python libraries, Claude skills, and Claude Code plugins with badges, CI/CD workflows, coverage metrics, media artifacts, and automatic plugin standards validation.
category: scaffolding
triggers:
  - /github-ready
aliases:
  - /github-ready
workflow_steps:
  - detect_package_type
  - analyze_existing_structure
  - select_package_template
  - validate_plugin_standards
  - scaffold_project_structure
  - configure_ci_cd
  - generate_badges
  - create_documentation
  - validate_package
  - cleanup_obsolete_files

suggest:
  - /init
  - /github-public-posting
---
# /github-ready — Universal Package Creator & Portfolio Polisher v5.6.0

## Purpose

**PRIMARY GOAL**: Create **Claude Code Plugins** for packages with hooks, skills, or Claude Code integration.

**SECONDARY GOAL**: Convert existing Python libraries to plugins (brownfield conversion).

**ADVANCED USE CASE**: Create pure Python backend libraries (pip-installable, no hooks/skills) — only when plugin architecture isn't appropriate.

All packages are polished into resume-worthy GitHub artifacts with badges, CI/CD workflows, coverage metrics, and media assets.

**v5.3 Update**: Integrated code-review plugin for automated quality validation before portfolio polish. Packages are now reviewed for security, performance, and maintainability issues before adding badges and CI/CD. More efficient workflow: fix quality issues before polishing.

**v5.2 Update**: Aligned with official Claude Code plugin structure. Plugins now follow best practices from hookify, context7, and plugin-dev: minimal plugin.json, core/ directory for Python code, hooks/hooks.json, .mcp.json for MCP, and optional commands/agents/skills directories.

**What this does:**
- **Scaffold**: Create canonical Claude Code Plugin structure (.claude-plugin/, core/, hooks/) by default
- **Convert**: Transform existing Python libraries to plugins (brownfield conversion)
- **Polish**: Transform repos into GitHub-ready portfolio artifacts (badges, CI/CD, CHANGELOG, metrics)
- **Detect**: Intelligent gap detection identifies what's missing
- **Generate**: Auto-create missing artifacts with evidence-based content

**Advanced**: Create pure Python backend libraries (pyproject.toml, src/, tests/) when plugin architecture isn't appropriate

## Bundled Resources

This skill includes utility scripts and reference documentation:

**Scripts** (`resources/`):
- `badge_generator.py` - Generate badges from shields.io
- `check_standards.py` - Validate package standards compliance
- `standards_compliance.py` - Check Python/Claude skill standards
- `recruiter_checklist.py` - Portfolio optimization checklist

**Templates** (`resources/`):
- `AGENTS.template.md` - AGENTS.md template for AI-maintainable documentation

**Reference Documentation** (`resources/`):
- `BADGE_GENERATION_GUIDE.md` - Complete badge generation guide
- `STANDARDS_VALIDATION.md` - Standards reference
- `V5.2_UPDATE_SUMMARY.md` - v5.1 → v5.2 changes

**Additional References** (`references/`):
- `brownfield-conversion.md` - Python library to plugin conversion
- `plugin-environment.md` - CLAUDE_PLUGIN_ROOT usage guide

## Project Context

### Constitution/Constraints
- Per CLAUDE.md: Solo-dev environment with pragmatic solutions
- **DEFAULT**: Claude Code Plugins for packages with hooks/skills (`.claude-plugin/`, `core/`, `hooks/`)
- **MIGRATION**: Convert existing Python libraries to plugins via brownfield conversion
- **ADVANCED**: Pure Python libraries (pyproject.toml, src layout) only for backend code without Claude Code integration
- Windows-compatible links: **Junctions for skill directories** (no admin required, Git-compatible), **Symlinks for individual files** (requires admin or Developer Mode)
  - **CRITICAL**: When using junctions for skill development, add the **junction target** to `.gitignore` to prevent dual git tracking
  - Pattern: Track source (`packages/<name>/skill/`), ignore junction target (`.claude/skills/<name>/`)
  - See: `P:/.claude/arch_decisions/2026-03-16_arch-skill-junction-git-strategy.md`
- Truthfulness required: Only claim what actually exists, don't fabricate features

### Technical Context
- **DEFAULT**: Claude Code Plugins (`.claude-plugin/`, `core/`, `hooks/`) for packages with hooks/skills
- **CONVERSION**: Brownfield Python library → Plugin conversion (src/ → core/)
- **ADVANCED**: Pure Python libraries (`src/`, `pyproject.toml`) for backend-only code (no hooks/skills)
- Portfolio-quality README with badges, architecture flowchart, Quick Start
- CI/CD workflows with status badges (Python libraries only)
- NotebookLM integration for AI-generated explainer videos and diagrams

### CLAUDE_PLUGIN_ROOT Environment Variable

`CLAUDE_PLUGIN_ROOT` is an environment variable pointing to the plugin's installation directory. Use it in all hook and MCP paths for portability across installation methods (marketplace, local, development).

**See `references/plugin-environment.md`** for complete usage guide.

### Architecture Alignment
- Integrates with `//p-2025` for Python standards
- Works with `/init` for CLAUDE.md initialization
- Integrates with `/github-public-posting` for pre-publish checks

## Your Workflow

**One command → Full intelligent pipeline:**

1. **DETECT** — Scan repository, identify gaps and needs
2. **ANALYZE** — Determine package type automatically
3. **GENERATE** — Create all missing artifacts (structure, badges, CI/CD, docs, CHANGELOG)
4. **VALIDATE** — Verify everything works
5. **CLEANUP** — Detect and remove obsolete files from refactoring
6. **REPORT** — Show what was created with evidence

**No manual phase selection required.** The skill detects what's needed and does it.

**Override flags (rarely needed):**
- `--dry-run` — Preview without creating
- `--skip <phase>` — Skip specific phase (e.g., `--skip media`)
- `--check-only` — Analyze without creating

---

## Philosophy: Intelligent Defaults

**Everything enabled by default.** The skill detects what's needed and walks through all appropriate phases automatically.

```bash
/package                          # Full pipeline: detect → scaffold → polish → validate
/package <name>                   # Same, with specific package name
/package --dry-run                # Preview what will happen
/package --skip <phase>           # Skip specific phase (e.g., --skip media)
```

**What it does automatically:**
1. Detects if new package or existing repo
2. Creates structure if needed
3. Generates all portfolio artifacts (badges, CI/CD, docs, CHANGELOG)
4. Collects metrics and generates badges
5. Validates everything
6. Reports what was done

**Explicit overrides (rarely needed):**
```bash
/package --check-only            # Only review, don't create anything
/package --scaffold-only          # Only create structure, skip polish
/package --target <path>          # Work on specific directory
```

---

## Usage

```bash
# Default: Full intelligent pipeline
/package mylib                   # Detects type, scaffolds, polishes, validates

# Preview mode
/package --dry-run mylib         # Show what will happen

# Skip specific phases
/package mylib --skip media      # Skip NotebookLM media generation
/package mylib --skip badges     # Skip badge generation

# Explicit target (current directory default)
/package --target P:/packages/existing-repo

# Review-only mode
/package --check-only            # Analyze without creating
```

---

## Intent Interpreter

**Simplified interface:** One command does everything. No mode selection required.

| User says | Action |
|-----------|--------|
| `/package` | Run full pipeline on current directory |
| `/package <name>` | Run full pipeline, create new package |
| `/package --dry-run` | Preview what will happen |
| `/package --skip <phase>` | Run full pipeline, skip specific phase |
| `/package --check-only` | Only analyze, don't create anything |

**Target detection:**
- Bare path: `/package P:/packages/mylib` → `--target P:/packages/mylib`
- `for <path>` → `--target <path>`
- Default: current directory

---

## PHASE 0: Dry Run Preview (Optional)

**Objective**: Preview what will be created without writing any files.

**Trigger**: `/package --dry-run [name]` or `/package polish --dry-run`

### What Dry Run Shows

```
=== PACKAGE DRY RUN ===

Mode: create / polish
Target Directory: {{TARGET_DIR}}
Package Name: {{NAME}}

=== Directory Structure ===
{{Tree view of structure}}

=== Files to Create ===
{{List of files with purposes}}

=== Next Steps ===
To proceed, run:
  /package {{NAME}}
```

---

## PHASE 1: Diagnose & Prep (30s)

**Objective**: Clear interference sources before building.

**Steps:**

1. **Check existing structure**:
```bash
tree {{TARGET_DIR}} -a -L 3 > {{TARGET_DIR}}/pre-pack-tree.txt
```

2. **Clear state files** (prevents state propagation stalls):
```bash
rm -f {{TARGET_DIR}}/.claude/state*.json
rm -f {{TARGET_DIR}}/.claude/checkpoints/*.json
```

3. **Check for existing modules**:
```bash
ls {{TARGET_DIR}}/src/ 2>/dev/null && echo "Modules: YES" || echo "Modules: NO"
```

**Output**: "Prep complete. Modules: [Y/N]. State cleared."

---

## PHASE 1.5: Detect Package Type (30s)

**Objective**: Determine if this is a Claude skill, Python library, Claude Code plugin, Claude Code plugin with MCP server, or hook-based package.

**Detection logic:**

```bash
# Check for SKILL.md (Claude skill marker)
if [ -f "{{TARGET_DIR}}/skill/SKILL.md" ] || [ -f "{{TARGET_DIR}}/SKILL.md" ]; then
    PACKAGE_TYPE="claude-skill"
    echo "Detected: Claude Skill"
# Check for .claude-plugin/ directory (Claude Code plugin with router integration)
elif [ -d "{{TARGET_DIR}}/.claude-plugin" ]; then
    PACKAGE_TYPE="claude-plugin"
    echo "Detected: Claude Code Plugin (with router integration)"

    # Check for MCP server
    if [ -f "{{TARGET_DIR}}/mcp_server.py" ] || [ -f "{{TARGET_DIR}}/mcp/server.py" ] || [ -d "{{TARGET_DIR}}/mcp" ]; then
        HAS_MCP_SERVER=true
        PACKAGE_TYPE="claude-plugin+mcp"
        echo "→ MCP Server: DETECTED"
    else
        HAS_MCP_SERVER=false
        echo "→ MCP Server: NOT FOUND"
    fi
# Check for hook/ directory (hook-based package)
elif [ -d "{{TARGET_DIR}}/hook" ]; then
    PACKAGE_TYPE="hook-package"
    echo "Detected: Hook Package"
# Check for Python library (src/ or pyproject.toml)
elif [ -d "{{TARGET_DIR}}/src" ] || [ -f "{{TARGET_DIR}}/pyproject.toml" ]; then
    PACKAGE_TYPE="python-library"
    echo "Detected: Python Library"

    # BROWNFIELD DETECTION: Check if Python library can be converted to plugin
    if [ -d "{{TARGET_DIR}}/src" ] && [ -f "{{TARGET_DIR}}/pyproject.toml" ]; then
        echo ""
        echo "⚠️  Python library detected: src/{{NAME}}/ with pyproject.toml"
        echo "Convert to Claude Code plugin?"
        echo "  • Removes pip install requirement"
        echo "  • Auto-registers hooks"
        echo "  • Changes: src/ → core/, adds plugin.json/hooks.json"
        echo ""
        read -p "Convert to plugin? (y/n): " CONVERT_TO_PLUGIN
        if [ "$CONVERT_TO_PLUGIN" = "y" ]; then
            PACKAGE_TYPE="brownfield-plugin"
            echo "✓ Proceeding with brownfield conversion..."
            echo ""
            echo "Details: This will backup your current structure, migrate src/ to core/,"
            echo "remove pyproject.toml, and add plugin configuration files."
            echo "Rollback available if needed."
        else
            echo "→ Keeping as Python library"
        fi
    fi
else
    PACKAGE_TYPE="python-library"
    echo "Detected: Python Library (new)"
fi
```

**Package Types:**

| Type | Trigger | Structure | Use Case | Recommendation |
|------|---------|-----------|----------|----------------|
| `claude-plugin` | `.claude-plugin/` directory exists | `.claude-plugin/` + `core/` + `hooks/` + README | **DEFAULT**: Packages with hooks/skills | ✅ **Primary pattern** |
| `claude-plugin+mcp` | `.claude-plugin/` + `mcp_server.py` or `mcp/` | `.claude-plugin/` + `core/` + `hooks/` + `.mcp.json` | Plugins with MCP server | ✅ **For MCP integration** |
| `brownfield-plugin` | Python library + user confirms | `src/` → `core/` conversion | Convert existing Python lib to plugin | ✅ **Migration path** |
| `python-library` | `src/` or `pyproject.toml` exists (no conversion) | `src/{{NAME}}/` + `tests/` + pyproject.toml | ⚠️ **ADVANCED**: Pure backend code (no hooks/skills) | ⚠️ **Only when plugins inappropriate** |
| `claude-skill` | `SKILL.md` exists | `skill/` only (no `src/`, no pyproject.toml) | Standalone Claude skills | ℹ️ **For skill-only packages** |
| `hook-package` | `hook/` directory exists | `hook/` + README | Legacy hook distribution | ℹ️ **Use plugin pattern instead** |

---

## PHASE 1.6: Brownfield Conversion (2min) — ONLY IF `PACKAGE_TYPE=brownfield-plugin`⚠️ **CRITICAL**: Review `references/brownfield-conversion.md` FIRST before proceeding.

**Pre-Conversion Checklist** (5 items):
- [ ] Fix hardcoded paths (no `P:/`, `/Users/`, `C:/` in source code)
- [ ] Fix platform-specific code (`.sh` scripts need `.bat` equivalents)
- [ ] Add error handling and logging (no silent `except: pass` blocks)
- [ ] Verify dependencies (use existing libraries, avoid reinventing)
- [ ] Expand test coverage (unit + error paths + integration)

**Summary**: Converts existing Python library (`src/` → `core/`) to Claude Code plugin structure with backup, verification, and rollback support. See `references/brownfield-conversion.md` for detailed 7-step workflow.

**Rollback**: Backup created at `.backup/` before conversion. To rollback: `cp -r .backup/* . && rm -rf core/ .claude-plugin/`

### Post-Conversion Verification (CRITICAL)

After brownfield conversion, check for broken symlinks that may still point to old `src/` paths:

```bash
# Check for broken symlinks pointing to old src/ path
cd P:/.claude/hooks
ls -la | grep "src/"

# If found, remove and recreate them with correct core/ paths:
rm PreCompact_handoff_capture.py SessionStart_handoff_restore.py
cmd /c "mklink PreCompact_handoff_capture.py p:\packages\handoff\core\hooks\PreCompact_handoff_capture.py"
cmd /c "mklink SessionStart_handoff_restore.py p:\packages\handoff\core\hooks\SessionStart_handoff_restore.py"
```

**Common pitfall**: Symlinks in `P:/.claude/hooks/` may still point to old `src/handoff/hooks/` path after conversion. Must point to `core/hooks/`.

## PHASE 1.7: Plugin Standards Validation (Auto-invoked)

**Objective**: Validate existing files/folders against OFFICIAL Claude Code plugin standards and provide CRUD recommendations.

**When**: Automatically runs after PHASE 1.5 (Detect Package Type) completes, for ALL plugin package types.

**What this does**:
- Scans root directory for files/folders
- Compares against OFFICIAL plugin-dev:plugin-structure standards
- Identifies non-standard files that violate plugin conventions
- Provides CRUD recommendations (Create, Update, Delete)
- Offers auto-cleanup with confirmation
- **NO ARGUMENTS REQUIRED** - runs automatically

**Standards Source**: OFFICIAL Claude Code plugin documentation from:
- **plugin-dev:plugin-structure** (authoritative source)
- **plugin-dev:plugin-settings** (configuration reference)
- **plugin-dev:create-plugin** (creation workflow)

### OFFICIAL Claude Code Plugin Structure

**Required Directories**:
- **`.claude-plugin/`** - Plugin metadata (contains ONLY `plugin.json`)
- **Component dirs at ROOT** - `commands/`, `agents/`, `skills/`, `hooks/` (NOT nested in `.claude-plugin/`)

**Optional Directories** (created as needed):
- **`commands/`** - Slash commands (.md files)
- **`agents/`** - Subagent definitions (.md files)
- **`skills/`** - Agent skills (subdirectories with `SKILL.md`)
- **`hooks/`** - Hook configuration (`hooks.json`)
- **`scripts/`** - Helper scripts and utilities (Python code goes here)
- **`.github/`** - GitHub workflows

**⚠️ CRITICAL CORRECTION FROM v5.6.0**:
- ❌ **WRONG**: `core/` directory is NOT in official spec
- ✅ **CORRECT**: Python code in `scripts/` or component directories
- ✅ **CORRECT**: Components at ROOT level (not nested in `.claude-plugin/`)

**Required Files** (root):
- **`README.md`** - Portfolio documentation
- **`LICENSE`** - License file

**Optional Files** (root):
- **`CHANGELOG.md`**** - Version history
- **`AGENTS.md`**** - AI-maintainable documentation
- **`CONTRIBUTING.md`**** - Contribution guidelines
- **`.gitignore`**** - Version control exclusions

**FORBIDDEN Files** (violate plugin standards):
- **`pyproject.toml`** - Plugins don't use pip packaging
- **`setup.py`** - Plugins don't use pip packaging
- **`setup.cfg`** - Plugins don't use pip packaging
- **`core/`** directory - NOT in official plugin structure
- **`src/`** directory - Use appropriate component directories instead

### Detection Logic

```bash
# Scan root directory
cd {{TARGET_DIR}}
ROOT_ITEMS=$(find . -maxdepth 1 -type d ! -name ".*" ! -name "." | sort)
ROOT_FILES=$(find . -maxdepth 1 -type f ! -name ".*" | sort)

# Check for forbidden files
FORBIDDEN=""
if [ -f "pyproject.toml" ]; then
    FORBIDDEN="$FORBIDDEN\n❌ DELETE: pyproject.toml (plugins don't need pip packaging)"
fi
if [ -d "src" ]; then
    FORBIDDEN="$FORBIDDEN\n❌ DELETE/MIGRATE: src/ (use core/ for plugins)"
fi

# Check for non-standard files (artifact patterns)
TEMP_FILES=$(find . -maxdepth 1 -name "*SUMMARY*.md" -o -name "*REPORT*.md" -o -name "*CHECKLIST*.md" -o -name "*AUDIT*.md" -o -name "*TREE*.txt" -o -name "README_*.md" 2>/dev/null)
if [ -n "$TEMP_FILES" ]; then
    FORBIDDEN="$FORBIDDEN\n⚠️  MOVE TO docs/: Temporary documentation artifacts"
fi

# Check for test scripts in root
TEST_SCRIPTS=$(find . -maxdepth 1 -name "test_*.py" -o -name "verify_*.py" -o -name "analyze_*.py" -o -name "diagnose_*.py" 2>/dev/null)
if [ -n "$TEST_SCRIPTS" ]; then
    FORBIDDEN="$FORBIDDEN\n⚠️  MOVE TO tests/: Standalone test scripts"
fi

echo "$FORBIDDEN"
```

### CRUD Recommendations

**DELETE** (violates plugin standards):
- `pyproject.toml`, `setup.py`, `setup.cfg` - Plugins don't use pip
- `src/` directory - Wrong structure, use `core/`
- `*.backup`, `*.old`, `*.bak` - Backup files
- `test_*.py`, `verify_*.py`, `analyze_*.py` - Temporary test scripts
- `*SUMMARY*.md`, `*REPORT*.md`, `*CHECKLIST*.md` - Temporary documentation
- `*TREE*.txt`, `README_NEW.md` - Diagnostic artifacts
- `.coverage`, `coverage.json` - Generated coverage files

**MOVE TO `docs/`** (historical context, not root clutter):
- `*_STRUCTURE.md`, `*_AUDIT*.md`, `*_VALIDATION*.md`
- `*_BREAKDOWN*.md`, `*_FIX*.md`, `*_DATA*.md`
- `*_IMPLEMENTATION*.md`, `*_PHASE*.md`

**MOVE TO `tests/`** (test suite organization):
- `test_*.py` (if useful tests)
- `verify_*.py` (if verification scripts)
- Review bundles, test fixtures

**KEEP IN ROOT** (standard plugin files):
- `README.md`, `LICENSE`, `CHANGELOG.md`
- `AGENTS.md`, `CONTRIBUTING.md`, `.gitignore`

### Auto-Cleanup Script

```bash
#!/bin/bash
# Auto-cleanup non-standard plugin files

# Create docs/ if needed
mkdir -p docs tests/fixtures

# Delete forbidden files
rm -f pyproject.toml setup.py setup.cfg
rm -f *.backup *.old *.bak
rm -f *SUMMARY*.md *REPORT*.md *CHECKLIST*.md *AUDIT*.md
rm -f *TREE*.txt README_NEW.md
rm -f test_*.py verify_*.py analyze_*.py diagnose_*.py
rm -f .coverage coverage.json

# Move documentation to docs/
mv *_STRUCTURE.md docs/ 2>/dev/null || true
mv *_AUDIT*.md docs/ 2>/dev/null || true
mv *_VALIDATION*.md docs/ 2>/dev/null || true
mv *_DATA*.md docs/ 2>/dev/null || true
mv *_IMPLEMENTATION*.md docs/ 2>/dev/null || true
mv *_PHASE*.md docs/ 2>/dev/null || true
mv review_bundle_*.md tests/fixtures/ 2>/dev/null || true

echo "✓ Cleanup complete"
echo "  Deleted: $(grep -c "DELETE" <<<$FORBIDDEN) forbidden files"
echo "  Moved: $(grep -c "MOVE" <<<$FORBIDDEN) files to appropriate directories"
```

### Output Format

**PLUGIN_STANDARDS_REPORT.md**:
```markdown
# Plugin Standards Validation Report

## Package Type: claude-plugin
## Compliance Score: 85/100

### ✅ Standards Compliant
- .claude-plugin/ exists
- core/ directory present
- hooks/ configuration present
- README.md with badges

### ❌ Standards Violations (5 items)
- **DELETE**: pyproject.toml (plugins don't need pip packaging)
- **MOVE TO docs/**: HANDOFF_QUALITY_CHECKLIST.md (7 files)
- **MOVE TO tests/**: test_handoff_save_direct.py (2 files)
- **DELETE**: pre-pack-tree.txt (diagnostic artifact)

### 🚀 Auto-Cleanup Available
Run this command to auto-fix all violations:
```bash
cd P:/packages/handoff && bash cleanup_plugin_standards.sh
```

### 📋 Manual Cleanup Required
None - all violations can be auto-fixed.
```

**Integration**: Runs automatically after package type detection, before structure building. Can be invoked standalone with `/github-ready --check-standards`.

---

## PHASE 2: Build Structure (2min)

**Objective**: Create appropriate directory structure based on package type.

**⚠️ ARCHITECTURE GUIDANCE**:
- **DEFAULT**: Create Claude Code Plugins (`.claude-plugin/`, `core/`, `hooks/`) for packages with hooks/skills
- **MIGRATION**: Convert existing Python libraries to plugins via brownfield conversion
- **ADVANCED**: Create pure Python libraries only when plugin architecture isn't appropriate (e.g., pure backend code with no Claude Code integration)

### For Claude Skills (`PACKAGE_TYPE=claude-skill`)

**Standalone Claude Skill structure** (not part of a plugin):

```
{{TARGET_DIR}}/
├── skill/                     # Single source of truth
│   ├── SKILL.md              # Skill definition
│   ├── resources/            # Templates, configs
│   ├── scripts/              # Hook scripts, utility scripts
│   ├── tests/                # Test suite (optional)
│   └── *.py                  # Python modules (if any)
├── README.md
├── LICENSE
└── .gitignore
```

**IMPORTANT**: Claude skills do NOT need `pyproject.toml`. They are distributed as:
- Skills: Via junctions (Windows) or symlinks (macOS/Linux) from `skill/` to `~/.claude/skills/skill-name/`
- Hooks: Referenced in `~/.claude/settings.local.json`
- NOT pip-installable (no `src/`, no Python package)

**Steps:**

1. **Create directory structure**:
```bash
mkdir -p {{TARGET_DIR}}/skill
```

2. **Generate README.md** (see PHASE 3 templates)
3. **Create LICENSE** (MIT by default)
4. **Create scripts/install-dev.bat** (Windows junction automation)

### For Claude Code Plugins (`PACKAGE_TYPE=claude-plugin`)

**Official Claude Code plugin structure following best practices.**

```
{{TARGET_DIR}}/
├── .claude-plugin/            # Plugin metadata
│   └── plugin.json            # Minimal manifest
├── commands/                  # OPTIONAL: Slash commands (.md files)
├── agents/                    # OPTIONAL: Subagents (.md files)
├── skills/                    # OPTIONAL: Auto-activating skills
│   └── skill-name/
│       └── SKILL.md
├── hooks/
│   └── hooks.json             # Hook configuration
├── core/                      # Python code
│   ├── __init__.py
│   ├── main.py
│   └── utils/
{% if HAS_MCP_SERVER %}
├── .mcp.json                  # MCP server config
{% endif %}
├── scripts/                   # OPTIONAL: Helper scripts
├── tests/
├── .gitignore
├── README.md
└── LICENSE
```

**IMPORTANT**: Claude Code plugins use auto-discovered components:
- `.claude-plugin/plugin.json` - Minimal manifest (name, description, author)
- Components at ROOT level - commands/, agents/, skills/, hooks/
- `core/` directory - Python code (NOT packages/hook/)
{% if HAS_MCP_SERVER %}
- `.mcp.json` - MCP server configuration (NOT mcp/ directory)
{% endif %}
- NO pyproject.toml - Plugins are not pip packages
- CLAUDE_PLUGIN_ROOT - Use for all path references (portability)

**Component directories are OPTIONAL** - only create what you need.

**Steps:**

1. **Create directory structure**:
```bash
mkdir -p {{TARGET_DIR}}/.claude-plugin
mkdir -p {{TARGET_DIR}}/core
mkdir -p {{TARGET_DIR}}/hooks
mkdir -p {{TARGET_DIR}}/tests
# Optional directories (create if needed)
# mkdir -p {{TARGET_DIR}}/commands
# mkdir -p {{TARGET_DIR}}/agents
# mkdir -p {{TARGET_DIR}}/skills
# mkdir -p {{TARGET_DIR}}/scripts
```

2. **Create `.claude-plugin/plugin.json`**:
```json
{
  "name": "{{package_name}}",
  "description": "{{DESCRIPTION}}",
  "author": {
    "name": "{{AUTHOR_NAME}}",
    "email": "{{AUTHOR_EMAIL}}"
  }
}
```

3. **Create `hooks/hooks.json`** (if needed):
```json
{
  "{{HOOK_POINT}}": [{
    "matcher": ".*",
    "hooks": [{
      "type": "command",
      "command": "python CLAUDE_PLUGIN_ROOT/core/main.py"
    }]
  }]
}
```

{% if HAS_MCP_SERVER %}
4. **Create `.mcp.json`** (if HAS_MCP_SERVER):
```json
{
  "{{package_name}}": {
    "command": "python",
    "args": ["-m", "core.mcp.server"]
  }
}
```
{% endif %}
4. **Create `core/__init__.py`**: (Python initialization)
5. **Create `.gitignore`**: (Exclude .local.md files)
6. **Generate README.md** (see PHASE 3 templates)
7. **Create LICENSE** (MIT)

### Local Development Setup

**IMPORTANT: Three different deployment models for Claude Code:**

---

## **1. SKILLS (Dev Deployment)**

**For:** Packages with `skill/SKILL.md` directory

**Setup:**
```powershell
# Windows (Junction - Recommended, no admin required)
New-Item -ItemType Junction -Path "P:\.claude\skills\{{package_name}}" -Target "P:\packages\{{package_name}}\skill"

# macOS/Linux (Symlink)
ln -s /path/to/packages/{{package_name}}/skill ~/.claude/skills/{{package_name}}
```

**Key points:**
- ✅ Junction the entire `skill/` directory
- ✅ Skills auto-discovered from `P:/.claude/skills/`
- ✅ Edit in your package, changes work immediately

---

## **2. HOOKS (Dev Deployment)**

**For:** Packages with hook files (`.py` files in `core/hooks/`)

**Setup:**
```powershell
# Symlinks go in P:/.claude/hooks/ (NOT ~/.claude/plugins/)
cd P:/.claude/hooks

# Symlink individual hook files from your package
ln -sf P:/packages/{{package_name}}/core/hooks/HookName.py HookName.py
```

**Key points:**
- ✅ Symlink individual `.py` hook files only
- ✅ NOT the entire directory - just the `.py` files
- ✅ Symlinks go in `P:/.claude/hooks/` (NOT `~/.claude/plugins/`)
- ✅ These are dev-only symlinks for working directly on source code
- ✅ Routers or settings.json register the symlinks as actual code

---

## **3. PLUGINS (End User Deployment)**

**For:** Distribution to end users via marketplace or GitHub

**Setup:**
```bash
# End users install via /plugin command
/plugin P:/packages/{{package_name}}

# Or from marketplace
/plugin install {{package_name}}
```

**Key points:**
- ✅ Plugin copied to `~/.claude/plugins/cache/`
- ✅ Registered in `~/.claude/plugins/installed_plugins.json`
- ✅ **NOT for local development** - requires reinstall on every change
- ✅ Use for distributing finished packages to users

---

## **Which Model Does Your Package Need?**

| Package Type | Dev Setup | End User Setup |
|--------------|-----------|----------------|
| **Skill only** | Skill junction | N/A (skill dev = use) |
| **Hooks only** | Hook symlinks | `/plugin` command |
| **Skill + Hooks** | Both | `/plugin` command |
| **Plugin** | Plugin junction to `~/.claude/plugins/local/` | `/plugin` command |

**Common Mistakes:**
- ❌ Don't use `/plugin` command for local development (requires reinstall on every change)
- ❌ Don't symlink entire directories to `P:/claude/hooks/` (only symlink `.py` files)
- ❌ Don't confuse skills (`P:/.claude/skills/`) with plugins (`~/.claude/plugins/`)
- ❌ Don't look for hook symlinks in `~/.claude/plugins/` - they go in `P:/.claude/hooks/`
- ❌ Don't forget to update symlinks after brownfield conversion - check for `src/` paths

### Multiple Skills or Hooks

Some plugins have **multiple skills** or **multiple hook files**. In these cases, you need **one junction per skill** and **one symlink per hook file**.

#### Multiple Skills (One Junction Per Skill)

If your plugin has multiple skills in `skills/`:

```
my-plugin/
├── skills/
│   ├── skill-a/SKILL.md  → Junction 1
│   ├── skill-b/SKILL.md  → Junction 2
│   └── skill-c/SKILL.md  → Junction 3
```

Create **one junction for each skill**:

```powershell
# Example: Plugin with 3 skills
New-Item -ItemType Junction -Path "P:\.claude\skills\skill-a" -Target "P:\packages\my-plugin\skills\skill-a"
New-Item -ItemType Junction -Path "P:\.claude\skills\skill-b" -Target "P:\packages\my-plugin\skills\skill-b"
New-Item -ItemType Junction -Path "P:\.claude\skills\skill-c" -Target "P:\packages\my-plugin\skills\skill-c"
```

**macOS/Linux equivalent:**
```bash
ln -s /path/to/packages/my-plugin/skills/skill-a ~/.claude/skills/skill-a
ln -s /path/to/packages/my-plugin/skills/skill-b ~/.claude/skills/skill-b
ln -s /path/to/packages/my-plugin/skills/skill-c ~/.claude/skills/skill-c
```

#### Multiple Hook Files (One Symlink Per File)

If your plugin has multiple hook files in `core/hooks/`:

```
my-plugin/
└── core/
    └── hooks/
        ├── hook1.py  → Symlink 1
        ├── hook2.py  → Symlink 2
        └── hook3.py  → Symlink 3
```

Create **one symlink for each hook file**:

```powershell
# Symlinks go in P:/.claude/hooks/ (NOT ~/.claude/plugins/)
cd P:/.claude/hooks

cmd /c "mklink hook1.py P:\packages\my-plugin\core\hooks\hook1.py"
cmd /c "mklink hook2.py P:\packages\my-plugin\core\hooks\hook2.py"
cmd /c "mklink hook3.py P:\packages\my-plugin\core\hooks\hook3.py"
```

**macOS/Linux equivalent:**
```bash
cd ~/.claude/hooks
ln -sf /path/to/packages/my-plugin/core/hooks/hook1.py hook1.py
ln -sf /path/to/packages/my-plugin/core/hooks/hook2.py hook2.py
ln -sf /path/to/packages/my-plugin/core/hooks/hook3.py hook3.py
```

#### Both Skills AND Hooks

If your plugin has **both skills and hooks**, create both junctions and symlinks:

```
my-plugin/
├── skills/
│   ├── skill-a/SKILL.md  → Junction to skills/skill-a/
│   └── skill-b/SKILL.md  → Junction to skills/skill-b/
└── core/
    └── hooks/
        ├── hook1.py  → Symlink in P:/.claude/hooks/
        └── hook2.py  → Symlink in P:/.claude/hooks/
```

**Complete setup:**
```powershell
# 1. Create junctions for skills (one per skill)
New-Item -ItemType Junction -Path "P:\.claude\skills\skill-a" -Target "P:\packages\my-plugin\skills\skill-a"
New-Item -ItemType Junction -Path "P:\.claude\skills\skill-b" -Target "P:\packages\my-plugin\skills\skill-b"

# 2. Create symlinks for hook files (one per file)
cd P:/.claude/hooks
cmd /c "mklink hook1.py P:\packages\my-plugin\core\hooks\hook1.py"
cmd /c "mklink hook2.py P:\packages\my-plugin\core\hooks\hook2.py"
```

**Real-world example: github-ready package**

The github-ready package has:
- 1 skill: `skills/github-ready/SKILL.md`
- 0 hooks (no hook files)

Setup:
```powershell
# Just one junction needed
New-Item -ItemType Junction -Path "P:\.claude\skills\package" -Target "P:\packages\github-ready\skills\github-ready"
```

**Summary table:**

| Plugin has... | Link type | How many? | Where? |
|---------------|-----------|-----------|--------|
| 1 skill | Junction | 1 | `P:/.claude/skills/skill-name` |
| 3 skills | Junctions | 3 (one per skill) | `P:/.claude/skills/skill-a`, `skill-b`, `skill-c` |
| 1 hook file | Symlink | 1 | `P:/.claude/hooks/hook.py` |
| 5 hook files | Symlinks | 5 (one per file) | `P:/.claude/hooks/hook1.py` through `hook5.py` |
| 2 skills + 3 hooks | Both | 2 junctions + 3 symlinks | Skills → `P:/.claude/skills/`, Hooks → `P:/.claude/hooks/` |

### For Python Libraries (`PACKAGE_TYPE=python-library`)

**Steps:**

1. **Create directory structure**:
```bash
mkdir -p {{TARGET_DIR}}/src/{{NAME}}
mkdir -p {{TARGET_DIR}}/tests
touch {{TARGET_DIR}}/src/{{NAME}}/__init__.py
touch {{TARGET_DIR}}/tests/__init__.py
```

2. **Generate README.md** (see PHASE 3 templates)
3. **Create LICENSE** (MIT)
4. **Create pyproject.toml** (full Python package)
5. **Create CONTRIBUTING.md**
6. **Create SECURITY.md**

---

## PHASE 3: Generate Templates

**Objective**: Generate README.md, LICENSE, AGENTS.md, and configuration files based on package type.

**Templates auto-generated**:
- **Python libraries**: pip install instructions, Quick Start, development setup
- **Claude skills**: Manual installation via junctions/symlinks, no pyproject.toml
- **Claude Code plugins**: `/plugin` installation, local dev with junctions/symlinks
- **Brownfield plugins**: Migration notice, rollback instructions, updated usage examples

**All packages get AGENTS.md**:
- AI-maintainable documentation for Claude, Copilot, and other AI assistants
- Uses template from `resources/AGENTS.template.md`
- Documents plugin constraints, setup commands, and development workflows
- Critical for long-term maintainability by AI assistants

### README Structure Contract

**CRITICAL**: Keep the main `README.md` as the source of truth for package documentation. Use GitHub Pages only for browser playback of the explainer video unless the user explicitly asks for a separate docs site.

**Required top-level README order:**
1. Project title, badges, and one-paragraph overview
2. `Quick Start`
3. `Explainer Video`
4. `What {{package_name}} Does`
5. `Development and Deployment`
6. `Additional Media Assets`
7. Lower-priority reference sections such as package types, contributing, changelog, and resources

**Rules:**
- Put the explainer video immediately after `Quick Start`
- Keep architecture, workflow, and usage details on the main GitHub page
- Generate `docs/video.html` for GitHub Pages by default
- Do not generate extra Pages docs such as `docs/*architecture*.html` or `docs/*workflow*.html` unless the user explicitly asks for them
- Link the README poster image to the GitHub Pages player page and keep all other technical content in the repository README

### README Template for Claude Code Plugins

**CRITICAL**: Include the "Three Deployment Models" section in every generated README.md to prevent confusion about installation methods.

```markdown
## Installation

### Three Deployment Models

**IMPORTANT**: This package supports three different deployment modes. Choose the right one for your use case.

#### 1. SKILLS (Dev Deployment) ⭐ **Recommended for Development**

**For**: When you're actively developing this package and want instant feedback.

**Setup:**
\`\`\`powershell
# Windows (Junction - No admin required)
# For plugins with skills: Junction to the skills/ subdirectory
New-Item -ItemType Junction -Path "P:\.claude\skills\{{package_name}}" -Target "P:\packages\{{package_name}}\skills\{{package_name}}"

# For standalone skills (skill/ directory): Junction to the skill/ subdirectory
# New-Item -ItemType Junction -Path "P:\.claude\skills\{{package_name}}" -Target "P:\packages\{{package_name}}\skill"

# macOS/Linux (Symlink)
ln -s /path/to/packages/{{package_name}}/skills/{{package_name}} ~/.claude/skills/{{package_name}}
\`\`\`

**Key points:**
- ✅ Edit in \`P:/packages/{{package_name}}\`, changes work immediately
- ✅ No reinstallation required - skills auto-discover from \`P:/.claude/skills/\`
- ✅ Perfect for active development
- ✅ Junction to `skills/{{package_name}}/` for plugin skills, or `skill/` for standalone skills
- ⚠️  **CRITICAL**: The junction target must point to WHERE THE SKILL.md FILE ACTUALLY LIVES:
  - Plugin skills: `package-name/skills/skill-name/SKILL.md` → junction target: `skills/skill-name/`
  - Standalone skills: `package-name/skill/SKILL.md` → junction target: `skill/`

**Important Note on Skill Naming:**
- The junction NAME (`{{package_name}}`) should match the skill directory name in the package
- This ensures the skill URL (`/skill-name`) works correctly
- Example: If package has `skills/my-skill/SKILL.md`, create junction as `P:/.claude/skills/my-skill/`
- The skill's **aliases** in the frontmatter determine what users type to invoke it

#### 2. HOOKS (Dev Deployment - Hook Files Only)

**For**: When this package has hook files (\`.py\` files in \`core/hooks/\`) you want to test.

**Setup:**
\`\`\`powershell
# Symlink individual hook files to P:/.claude/hooks/
cd P:/.claude/hooks

# Example: Symlink a specific hook file
cmd /c "mklink HookName.py P:/packages/{{package_name}}/core/hooks/HookName.py"
\`\`\`

**Key points:**
- ✅ Symlink individual \`.py\` hook files only (NOT the entire directory)
- ✅ Symlinks go in \`P:/.claude/hooks/\` (NOT \`~/.claude/plugins/\`)
- ✅ These are dev-only symlinks for working directly on source code
- ⚠️  After brownfield conversion, check for broken symlinks pointing to old \`src/\` paths

#### 3. PLUGINS (End User Deployment)

**For**: Distributing this package to other users via marketplace or GitHub.

**Setup:**
\`\`\`bash
# End users install via /plugin command
/plugin P:/packages/{{package_name}}

# Or from marketplace (when published)
/plugin install {{package_name}}
\`\`\`

**Key points:**
- ✅ Plugin copied to \`~/.claude/plugins/cache/\`
- ✅ Registered in \`~/.claude/plugins/installed_plugins.json\`
- ❌ **NOT for local development** - requires reinstall on every change
- ✅ Use for distributing finished packages to users

### Which Model Should You Use?

| Your Situation | Use This Model | Why |
|----------------|----------------|-----|
| Actively developing this package | **SKILLS** (junction) | Instant feedback, no reinstall |
| Testing hook file changes | **HOOKS** (symlinks) | Direct hook testing |
| Distributing to end users | **PLUGINS** (/plugin) | Proper distribution format |

### Common Mistakes to Avoid

- ❌ Don't use \`/plugin\` command for local development (requires reinstall on every change)
- ❌ Don't symlink entire directories to \`P:/.claude/hooks/\` (only symlink \`.py\` files)
- ❌ Don't confuse skills (\`P:/.claude/skills/\`) with plugins (\`~/.claude/plugins/\`)
- ❌ Don't forget to update symlinks after brownfield conversion - check for \`src/\` paths
\`\`\`

### Media Assets Section Template

**After media generation completes (PHASE 4.7), add this section to README.md after `Development and Deployment`:**

\`\`\`markdown
## Explainer Video

[![Watch the demo with audio](assets/videos/{{package_name}}_video_poster.png)](https://{{github_username}}.github.io/{{package_name}}/docs/video.html)

> **[🎬 Watch the explainer in the browser](https://{{github_username}}.github.io/{{package_name}}/docs/video.html)**
> **[⬇️ Download the MP4 directly](https://github.com/{{github_username}}/{{package_name}}/releases/download/media/{{package_name}}_explainer_pbs.mp4)**
> *Browser playback requires GitHub Pages to be enabled for this repository.*

Quick overview of features and workflow.

## Additional Media Assets

### 📊 Architecture Flowchart

```mermaid
graph TB
    Input[User: /{{package_name}}] --> Detect[Detect Package Type]
    Detect --> Type{Package Type?}
    Type -->|Plugin| Plugin[Plugin Structure]
    Type -->|Skill| Skill[Skill Structure]
    Type -->|Library| Library[Library Structure]
    Plugin --> Polish[Portfolio Polish]
    Skill --> Polish
    Library --> Polish
    Polish --> Docs[Documentation]
    Polish --> Media[Media Assets]
    Polish --> CI[CI/CD]
    Docs --> Output[GitHub-Ready Package]
    Media --> Output
    CI --> Output
```

### 📑 Presentation Slides

[![Slide deck preview](assets/slides/{{package_name}}_slides_preview.png)](assets/slides/{{package_name}}_slides.pdf)

**[📄 View Slides (PDF)](assets/slides/{{package_name}}_slides.pdf)**
**[⬇️ Download PDF](assets/slides/{{package_name}}_slides.pdf)**

*Use the PDF for both viewing and download on GitHub.*

---

**💡 Tip**: Use GitHub Pages for in-browser video playback. Keep the slide deck in PDF form for the cleanest GitHub viewing experience.
\`\`\`

**IMPORTANT**: This media layout uses GitHub-compatible markdown. Key points:
- **Images**: Use standard markdown \`![alt](path)\` syntax - renders inline
- **Videos**: Do not rely on HTML \`<video>\` tags in \`README.md\`
- **Recommended pattern**: Link a verified still frame such as \`assets/videos/{{package_name}}_video_poster.png\` in \`README.md\` to \`https://{{github_username}}.github.io/{{package_name}}/docs/video.html\`
- **Fallback**: Keep the release asset MP4 link for direct download/open
- **PDFs**: Use direct markdown links - opens in GitHub's built-in PDF viewer
- **Slide previews**: Export the first PDF page to \`assets/slides/{{package_name}}_slides_preview.png\` and link it to the PDF
- **Badges**: Use shields.io badges for visual appeal and clickability
- **GitHub Pages**: Enable Pages from \`main\` root so \`docs/video.html\` is publicly available
- **Pages scope**: Use GitHub Pages only for the video player by default; keep architecture and workflow documentation in \`README.md\`
- **Durations**: Never hardcode video runtimes. Measure the exported file first or omit the duration label entirely

**Runtime verification examples:**
```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 assets/videos/{{package_name}}_explainer_pbs.mp4
```

**For brownfield conversions**: See \`references/brownfield-conversion.md\` for README update instructions (migration notice, rollback instructions, updated usage examples).
## PHASE 4: Validate (1min)

**Objective**: Verify package structure is correct.

**Checks:**

1. **Platform compatibility check** (CRITICAL for Claude skills):
```bash
# Detect platform
PLATFORM="$(uname -s)"
case "$PLATFORM" in
  Linux*)     PLATFORM="linux" ;;
  Darwin*)    PLATFORM="macos" ;;
  MINGW*|MSYS*|CYGWIN*) PLATFORM="windows" ;;
  *)          PLATFORM="unknown" ;;
esac

# Check for deployment errors: Platform-specific docs referencing wrong scripts
if [ "$PLATFORM" = "windows" ]; then
  # Check Windows-specific documentation for .sh references in hook configs
  WINDOWS_DOCS=$(find {{TARGET_DIR}} -name "WINDOWS.md" -o -name "INSTALLATION.md" 2>/dev/null)

  if [ -n "$WINDOWS_DOCS" ]; then
    # Look for .sh files referenced in hook/command configurations
    SH_CONFIG_REFS=$(grep -n '"command".*\.sh' $WINDOWS_DOCS 2>/dev/null | grep -v "# " | grep -v "Unix\|Linux\|macOS\|Darwin")

    if [ -n "$SH_CONFIG_REFS" ]; then
      echo "❌ ERROR: Windows documentation references .sh scripts in hook configurations:"
      echo "$SH_CONFIG_REFS"
      echo ""
      echo "Problem: Windows users cannot execute .sh scripts natively without WSL/Git Bash"
      echo "Solution: Change .sh to .bat in hook configuration examples"
      echo ""
      echo "Example fix:"
      echo '  "command": "P:\\\\.claude\\skills\\reflect\\scripts\\hook-stop.sh"'
      echo "  → Should be:"
      echo '  "command": "P:\\\\.claude\\skills\\reflect\\scripts\\hook-stop.bat"'
    fi
  fi

  # Optional: Verify .bat/.ps1 alternatives exist for any .sh files in scripts/
  SH_SCRIPTS=$(find {{TARGET_DIR}} -name "*.sh" -path "*/scripts/*" 2>/dev/null)
  if [ -n "$SH_SCRIPTS" ]; then
    for sh_file in $SH_SCRIPTS; do
      bat_file="${sh_file%.sh}.bat"
      ps1_file="${sh_file%.sh}.ps1"
      if [ ! -f "$bat_file" ] && [ ! -f "$ps1_file" ]; then
        echo "⚠️  WARNING: $sh_file has no .bat or .ps1 equivalent for Windows users"
      fi
    done
  fi
fi
```

2. **Symlink test** (for Claude skills):
```bash
test -L ~/.claude/skills/{{NAME}} && echo "Symlink: OK" || echo "Symlink: MISSING"
```

3. **Pytest collect**:
```bash
pytest --collect-only {{TARGET_DIR}}/tests/
```

4. **Tree diff**:
```bash
tree {{TARGET_DIR}} -a -L 3 > {{TARGET_DIR}}/post-pack-tree.txt
diff {{TARGET_DIR}}/pre-pack-tree.txt {{TARGET_DIR}}/post-pack-tree.txt
```

**Output**: "Validation complete. All checks passed."

---

## PHASE 4.5: Code Review & Meta-Review (Auto-invoked) — UPDATED v5.4

**Objective**: Run automated code review AND meta-review to catch quality and cross-file issues before portfolio polish.

**When**: Automatically runs after PHASE 4 (Validate) completes, before PHASE 5 (Portfolio Polish).

**What this does:**
1. **Code Review Plugin**: Comprehensive code review with confidence-based scoring
   - Checks for security, performance, and maintainability issues
   - Confidence threshold (80+) for filtering findings
   - Generates summary report with actionable recommendations

2. **Meta-Review System**: Cross-file analysis for architectural issues
   - Path traversal vulnerability detection (taint propagation)
   - Import graph analysis (circular dependencies, layering violations)
   - Documentation consistency validation
   - AnalysisUnit-based manifest-driven review

**Execution:**
```python
# Code review (existing)
Skill(skill="code-review:code-review", args="{{TARGET_DIR}}")

# Meta-review (NEW - T-007 integration)
from lib.meta_review.prepare_context import prepare_agent_context
from lib.analysis_unit import create_analysis_unit

unit_id = create_analysis_unit(Path("{{TARGET_DIR}}"))
context = prepare_agent_context(unit_id, perspective="security", max_tokens=8000)

# Run meta-review analyzers
from lib.analysis_unit.analyzers.path_traversal import PathTraversalAnalyzer
from lib.analysis_unit.analyzers.import_graph import ImportGraphAnalyzer
from lib.analysis_unit.analyzers.doc_consistency import DocConsistencyAnalyzer

pt_findings = PathTraversalAnalyzer().analyze(manifest)["findings"]
ig_findings = ImportGraphAnalyzer().analyze(manifest)["findings"]
dc_findings = DocConsistencyAnalyzer(manifest).analyze()

# Combine findings
meta_review_summary = {
    "path_traversal": pt_findings,
    "import_graph": ig_findings,
    "doc_consistency": dc_findings,
    "total_findings": len(pt_findings) + len(ig_findings) + len(dc_findings)
}
```

**Integration notes:**
- Run AFTER structure validation passes
- Run BEFORE portfolio polish (prevents polishing bad code)
- Meta-review is optional (controlled by META_REVIEW_ENABLED env var, default: true)
- If critical findings (HIGH severity): fix before proceeding to PHASE 5
- If advisory findings (MEDIUM/LOW severity): document, proceed to PHASE 5
- If no findings: proceed to PHASE 5

**What gets reviewed:**
- Code review: Package structure, configuration files, Python code
- Meta-review: Cross-file issues, import graphs, path traversals, documentation consistency

**Duration**: 1-3 minutes (combined)

**Output**: Combined code review + meta-review summary with severity-tagged findings

**v5.4 Update**: Integrated meta-review system (T-007) alongside code-review plugin for comprehensive quality validation.

---

## PHASE 4.7: Media Generation (Auto-invoked) — NEW

**Objective**: Generate professional portfolio assets (banners, diagrams, videos) for GitHub showcase.

**When**: Automatically runs after PHASE 4.5 (Code Review) completes, before PHASE 5 (Portfolio Polish).

**What this does:**
- Generates visual assets for portfolio-quality packages
- Creates banner images for GitHub social preview
- Builds static overview images plus GitHub-safe Mermaid flowcharts
- Produces one concise technical explainer video focused on architecture, workflow, and outputs
- Creates a dedicated HTML video player page for GitHub Pages playback
- Verifies asset quality with vision API before acceptance

**Generated Assets:**

| Asset | Purpose | Tool | Time | Output Formats |
|-------|---------|------|------|---------------|
| **Banner** | GitHub social preview | OpenRouter | ~30s | `assets/banners/{package}_banner.png` |
| **Architecture overview image** | Visual system overview | NotebookLM | ~2min | `assets/infographics/{package}_architecture.png` |
| **System overview flowchart** | GitHub-safe architecture view | Mermaid | ~1min | `docs/diagrams/system_overview.mmd` |
| **Workflow flowchart** | Phase-by-phase pipeline view | Mermaid | ~1min | `docs/diagrams/workflow.mmd` |
| **Video player page** | Browser playback via GitHub Pages | Static HTML | ~30s | `docs/video.html` |
| **Explainer video** | AI-narrated technical walkthrough | NotebookLM | ~1-3min target | `assets/videos/{package}_explainer_pbs.mp4` |
| **Slide deck** | Interactive presentation | NotebookLM | ~2min | `assets/slides/{package}_slides.pdf` (view and download as PDF) |

**Auto-skip conditions:**
- No README images detected (`.gif`, `.png` in README)
- User explicitly opts out with `--skip media`

**Provider requirements:**
- **NotebookLM**: `uv tool install notebooklm-mcp-cli` (v0.4.4+) + `nlm login`
- **visual-explainer:generate-web-diagram**: Installed via `/universal-skills-manager` or ClawHub
- **OpenRouter**: `OPENROUTER_API_KEY` environment variable (for banner generation, optional)
- **NotebookLM**: `uv tool install notebooklm-mcp-cli` (v0.4.4+) + `nlm login`
- **OpenRouter**: `OPENROUTER_API_KEY` environment variable (for banner generation)

**If providers missing:**
- Check provider status and display clear setup instructions
- Skip assets that require unavailable providers
- Continue with available assets only

**Execution flow:**
```
Provider detection → Review bundle generation → Video brief generation → Multi-source upload (brief + review bundle + source files) → Asset generation (NotebookLM + video page) → Quality verification → Notebook cleanup
```

**Asset generation via nlm CLI (v0.4.4+):**

```bash
# After uploading sources to notebook, generate artifacts:
NOTEBOOK_ID="<your-notebook-id>"

# Create architecture diagram (infographic)
nlm infographic create "$NOTEBOOK_ID" --orientation landscape --detail standard --style professional --confirm

# Create explainer video
# Prefer a concise technical walkthrough, not a broad marketing script.
nlm video create "$NOTEBOOK_ID" --format explainer --style documentary --confirm

# Create slide deck
nlm slides create "$NOTEBOOK_ID" --slide-format detailed_deck --confirm

# Poll for completion (background task recommended)
nlm studio status "$NOTEBOOK_ID"

# Download completed artifacts
nlm download infographic "$NOTEBOOK_ID" --id "$ARTIFACT_ID" --output assets/infographics/{package}_notebooklm.png
nlm download video "$NOTEBOOK_ID" --id "$ARTIFACT_ID" --output assets/videos/{package}_explainer.mp4
nlm download slide-deck "$NOTEBOOK_ID" --id "$ARTIFACT_ID" --output assets/slides/{package}_slides.pdf
```

### Multi-Source Upload Strategy

**Why multiple sources matter:**
- Single README uploads produce generic assets lacking technical depth
- Review bundle provides architectural context and design intent
- Multiple source files provide NotebookLM with complete implementation details
- Better source material → More accurate, detailed, and professional assets
- Code examples, tests, and documentation improve asset quality significantly

**Hybrid approach (BEST): Review bundle + source files**

**Why this works better:**
- **Review bundle** = Executive summary with architecture, design intent, and component relationships
- **Source files** = Implementation details, concrete code examples, and actual behavior
- **Combined** = High-level understanding + low-level evidence = Best artifacts

**Source file identification:**

```bash
# Step 1: Generate review bundle (architectural context)
/review_bundle {{TARGET_DIR}}

# Step 2: Find all relevant source files (excludes cache, build artifacts, venv, templates)
cd {{TARGET_DIR}}

# CRITICAL: Upload actual IMPLEMENTATION FILES, not just documentation
# Core package structure MUST be included:
# - Python source files (*.py) - the actual implementation
# - Plugin metadata (.claude-plugin/plugin.json, hooks/hooks.json)
# - Core configuration files
# - Tests
# - Key documentation (README, skill docs)

# EXCLUDE template/legal files:
# - CONTRIBUTING.md, SECURITY.md, LICENSE - generic templates
# - CHANGELOG.md - version history only
# - *-tree.txt - diagnostic output files
# - Cache, build artifacts, venv

# Priority files (upload these AFTER review bundle):
find . -type f \( -name "*.py" -o -name "SKILL.md" -o -name "plugin.json" -o -name "hooks.json" \) \
  ! -path "./.git/*" ! -path "./__pycache__/*" ! -path "./venv/*" \
  ! -path "./.pytest_cache/*" ! -path "./.ruff_cache/*" | sort
```

**⚠️ CRITICAL: Upload implementation, NOT just templates!**

The most common mistake is uploading only documentation files (README, CHANGELOG, etc.) without the actual Python source code. NotebookLM needs both:
1. **Architectural context** (review bundle) → What is this system and why does it exist?
2. **Implementation details** (source files) → How does it actually work?

**Priority upload order:**
1. **Review bundle** (generated via `/review_bundle`) - Architectural overview
2. **Core implementation** - `core/*.py`, `*.py` (the actual code)
3. **Plugin configuration** - `.claude-plugin/plugin.json`, `hooks/hooks.json`
4. **Tests** - `tests/*.py`
5. **Skill documentation** - `SKILL.md` (if exists)
6. **Key README** - README.md (package overview)
7. **Templates/guides** - Only if they explain IMPLEMENTATION details

**EXCLUSION patterns:**

**⚠️ QUICK CHECKLIST - Always exclude these:**
- ❌ Lock files: `package-lock.json`, `poetry.lock`, `requirements.lock`, `yarn.lock`, `Cargo.lock`
- ❌ Test outputs: `htmlcov/`, `coverage.xml`, `.coverage*`, `.pytest_cache/`
- ❌ Version control: `.git/`, `.gitignore`, `.gitattributes`
- ❌ Cache/build: `__pycache__/`, `*.pyc`, `build/`, `dist/`, `venv/`, `.venv/`
- ❌ Generic templates: `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`, `CHANGELOG.md`
- ❌ State/diagnostics: `*-tree.txt`, `.claude/state/`, `*.pid`
- ❌ Generated media: `assets/videos/*.mp4`, `assets/infographics/*.png`, `assets/slides/*`
- ❌ CI/CD config: `.github/workflows/`

---

**Version control & caches:**
- `.git/`, `.gitignore`, `.gitattributes` - Version control metadata
- `__pycache__/`, `*.pyc` - Python bytecode
- `.pytest_cache/`, `.ruff_cache/`, `.benchmarks/` - Tool caches

**State & diagnostics:**
- `.claude/state/`, `*.pid`, `state*.json` - Claude Code state files
- `*-tree.txt`, `pre-pack-tree.txt`, `post-pack-tree.txt` - Diagnostic outputs

**Build & artifacts:**
- `build/`, `dist/`, `*.egg-info/` - Build artifacts
- `venv/`, `.venv/` - Virtual environments

**CI/CD & infrastructure:**
- `.github/workflows/` - CI/CD configuration (not package logic)
- **Lock files (machine-generated dependency pinning):**
  - `package-lock.json` - npm/yarn lock files
  - `poetry.lock` - Poetry lock files
  - `requirements.lock`, `Pipfile.lock` - pip lock files
  - `yarn.lock`, `Cargo.lock`, `go.sum` - Other package manager locks

**IDE & temp files:**
- `.vscode/`, `.idea/`, `*.swp`, `*.swo` - IDE configuration
- `*.tmp`, `*.bak`, `*.backup`, `*.old` - Temporary/backup files

**Generic templates (NOT package-specific):**
- `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE` - Generic legal/templates
- `CHANGELOG.md` - Version history only (doesn't explain implementation)

**Generated outputs (OUTPUTS, not inputs):**
- `assets/videos/*.mp4`, `assets/infographics/*.png` - Media OUTPUTS
- `assets/slides/*` - Presentation OUTPUTS
- **Test outputs (machine-generated test artifacts):**
  - `htmlcov/`, `coverage.xml`, `.coverage*`, `.coverage.*` - Coverage reports
  - `.pytest_cache/` - Pytest cache
  - `test-results/`, `junit.xml` - Test result files
  - `.hypothesis/`, `.mypy_cache/` - Tool caches

**Binary artifacts:**
- `*.so`, `*.pyd`, `*.dll`, `*.exe` - Compiled binaries
- `*.zip`, `*.tar.gz`, `*.rar` - Compressed archives

**Upload process:**

```bash
# === STEP 1: Generate review bundle (architectural context) ===
echo "Generating review bundle for architectural context..."
Skill(skill="review_bundle", args="{{TARGET_DIR}}")

# Find the generated review bundle
REVIEW_BUNDLE=$(ls -t P:/__csf/.staging/review_bundle_*.md 2>/dev/null | head -1)
if [ -z "$REVIEW_BUNDLE" ]; then
  echo "⚠️  Warning: Review bundle not found, continuing without it"
else
  echo "✓ Review bundle generated: $REVIEW_BUNDLE"
fi

# === STEP 2: Create NotebookLM notebook with clear temporary naming ===
TEMP_NOTEBOOK_NAME="TEMP: {{package_name}} Media Generation [$(date +%Y%m%d_%H%M%S)]"
nlm notebook create "$TEMP_NOTEBOOK_NAME"
NOTEBOOK_ID=$(nlm notebook list | grep "$TEMP_NOTEBOOK_NAME" | head -1 | awk '{print $1}')

if [ -z "$NOTEBOOK_ID" ]; then
  echo "❌ Error: Failed to create notebook"
  exit 1
fi

echo "✓ Notebook created: $NOTEBOOK_ID"

# === STEP 3: Upload review bundle FIRST (architectural overview) ===
if [ -n "$REVIEW_BUNDLE" ] && [ -f "$REVIEW_BUNDLE" ]; then
  echo "Uploading review bundle..."
  nlm source add "$NOTEBOOK_ID" --file "$REVIEW_BUNDLE" --wait
  echo "✓ Review bundle uploaded"
fi

# === STEP 3.5: Upload a narration brief to control tone and length ===
cat > /tmp/video_brief.md <<'EOF'
# Video Brief

Create a concise technical explainer video for engineers evaluating this package.

Requirements:
- Tone: technical, calm, direct, low-hype
- Audience: developers, maintainers, technical reviewers
- Length target: 60 to 120 seconds
- Focus on:
  1. what the package does
  2. how the workflow operates
  3. what files and outputs it creates
  4. why the result is useful in practice
- Prefer concrete nouns and file paths over abstract claims
- Avoid marketing language, rhetorical questions, and dramatic setup
- Avoid extended "before/after pain" storytelling
- Avoid filler such as "imagine", "revolutionary", "seamless", "game-changing"
- End with a brief technical summary, not a call-to-action
EOF

nlm source add "$NOTEBOOK_ID" --file /tmp/video_brief.md --wait
echo "✓ Video brief uploaded"

# === STEP 4: Upload source files (implementation details) ===
# CRITICAL: Upload IMPLEMENTATION files FIRST, not just documentation!
# Priority: *.py > plugin.json > hooks.json > SKILL.md > README.md
#
# EXCLUDE (see QUICK CHECKLIST above):
# - Lock files: package-lock.json, poetry.lock, requirements.lock
# - Test outputs: htmlcov/, coverage.xml, .coverage*
# - Version control: .git/
# - Cache/build: __pycache__/, venv/, build/, dist/
# - Generic templates: CONTRIBUTING.md, SECURITY.md, LICENSE
# - State/diagnostics: *-tree.txt
# - Generated media: assets/videos/, assets/infographics/, assets/slides/
# - CI/CD config: .github/workflows/

echo "Uploading source files..."
find . -type f \( -name "*.py" -o -name "*.json" -o -name "SKILL.md" -o -name "README.md" \) \
  ! -path "./.git/*" \
  ! -path "./__pycache__/*" \
  ! -path "./venv/*" \
  ! -path "./.venv/*" \
  ! -path "./.pytest_cache/*" \
  ! -path "./.ruff_cache/*" \
  ! -path "./.benchmarks/*" \
  ! -path "./build/*" \
  ! -path "./dist/*" \
  ! -path "./.eggs/*" \
  ! -path "./htmlcov/*" \
  ! -path "./assets/videos/*" \
  ! -path "./assets/infographics/*" \
  ! -path "./assets/slides/*" \
  ! -path "./.github/workflows/*" \
  ! -name "package-lock.json" \
  ! -name "poetry.lock" \
  ! -name "requirements.lock" \
  ! -name "yarn.lock" \
  ! -name "Cargo.lock" \
  ! -name "*.egg-info/*" \
  ! -name "*-tree.txt" \
  ! -name ".coverage*" \
  ! -name "coverage.xml" \
  ! -name "junit.xml" | head -30 | \
  while read file; do
    echo "Uploading: $file"
    nlm source add "$NOTEBOOK_ID" --text "$(cat "$file")" --title "$(basename "$file")" --wait
  done

# === STEP 5: Upload key documentation (if not already included) ===
if [ -f "README.md" ]; then
  nlm source add "$NOTEBOOK_ID" --file README.md --wait 2>/dev/null || true
fi

# === STEP 6: Verify all sources uploaded ===
echo ""
echo "=== Sources uploaded to notebook $NOTEBOOK_ID ==="
nlm source list "$NOTEBOOK_ID"
echo ""

# === STEP 7: NOW generate assets (only after ALL uploads complete) ===
echo "Starting asset generation..."


### Video Compliance Verification & Regeneration (Option B Pipeline)

**Objective**: Verify generated videos comply with technical writing standards and regenerate non-compliant videos using Option B (Script → TTS → ffmpeg).

**When**: Automatically runs after video download (NotebookLM generation completes).

**Why this matters**: NotebookLM videos often contain casual language ("cool", "awesome", "super") even with technical briefs. Option B provides full control over compliance with faster iteration than regenerating via NotebookLM.

**Compliance standards**:
- **Absolutely forbidden**: "cool", "awesome", "super", "amazing", "ultra", "mega", "neat", "nifty", "handy", "sweet", "sick", "dope", "fire"
- **Marketing hype**: "game-changing", "revolutionary", "seamless", "transformative"
- **Anti-patterns**: "imagine", "picture this", "envision"

**Verification workflow with faster-whisper**:

```bash
# Step 1: Install faster-whisper if not available
pip install faster-whisper

# Step 2: Transcribe and verify video compliance
python << 'VERIFY_EOF'
from faster_whisper import WhisperModel
import json
import re

FORBIDDEN_PATTERNS = [
    r'super', r'cool', r'awesome', r'amazing',
    r'ultra', r'mega', r'neat', r'nifty',
    r'handy', r'sweet', r'sick', r'dope',
    r'fire', r'game.?changing', r'revolutionary',
    r'seamless', r'transformative', r'imagine',
    r'picture this', r'envision'
]

def check_compliance(text):
    violations = []
    text_lower = text.lower()
    for pattern in FORBIDDEN_PATTERNS:
        matches = re.finditer(pattern, text_lower, re.IGNORECASE)
        for match in matches:
            violations.append({
                'word': match.group(),
                'position': match.start(),
                'context': text[max(0, match.start()-30):min(len(text), match.end()+30)]
            })
    return violations

# Transcribe
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe("assets/videos/{package}_explainer.mp4", beam_size=5)

# Check violations
all_violations = []
for segment in segments:
    violations = check_compliance(segment.text.strip())
    for v in violations:
        all_violations.append({**v, 'time': f"{segment.start:.1f}-{segment.end:.1f}s"})

# Save transcript with violations
with open('assets/videos/{package}_transcript.json', 'w') as f:
    json.dump({'violations': all_violations, 'count': len(all_violations)}, f)

# Report
if all_violations:
    print(f"❌ FAILED: {len(all_violations)} violations found")
    exit(1)
else:
    print("✅ PASSED: No forbidden words")
    exit(0)
VERIFY_EOF
```

**Option B regeneration pipeline** (if violations found):

```bash
# Step 1: Generate compliant script (no forbidden words)
cat > assets/scripts/{package}_compliant_script.txt << 'SCRIPT_EOF'
[Write technical script without forbidden words]
SCRIPT_EOF

# Step 2: Install free TTS (edge-tts)
pip install edge-tts

# Step 3: Generate compliant audio
edge-tts --file assets/scripts/{package}_compliant_script.txt   --write-media assets/audio/{package}_compliant_audio.mp3

# Step 4: Replace audio track using ffmpeg
ffmpeg -i assets/videos/{package}_explainer.mp4   -i assets/audio/{package}_compliant_audio.mp3   -c:v copy -map 0:v:0 -map 1:a:0 -shortest   assets/videos/{package}_compliant.mp4 -y

# Step 5: Re-verify compliance
# Run faster-whisper verification again on compliant video
```

**Decision factors**:
- **Speed**: Option B (2-3 minutes) vs NotebookLM regeneration (5-10 minutes + uncertain)
- **Control**: Full script control vs AI generation variability
- **Cost**: Free (edge-tts) vs NotebookLM credits
- **Iteration**: Script changes are instant vs re-uploading sources to NotebookLM

**Duration**: ~3-5 minutes for full verification + regeneration (if needed)

**Output**:
- `assets/videos/{package}_transcript.json` - Transcript with violation markers
- `assets/videos/{package}_compliant.mp4` - Compliant video (0 violations)
- Verification report with violation count and locations

**Integration**: Runs automatically after video download, before notebook cleanup



**Notebook cleanup after asset generation:**

```bash
# ⚠️  SAFETY: This cleanup is OPTIONAL and MANUAL
# Review the matched notebook ID before running to ensure it's the correct one

# After generating all assets, you can clean up the temporary notebook
# Step 1: List all notebooks to see what exists
echo "Current notebooks:"
nlm notebook list

# Step 2: Find the temporary notebook by name pattern
NOTEBOOK_ID=$(nlm notebook list | grep "TEMP: {{package_name}} Media Generation" | head -1 | awk '{print $1}')

# Step 3: Show what would be deleted (SAFETY CHECK)
if [ -n "$NOTEBOOK_ID" ]; then
  echo "Found temporary notebook: $NOTEBOOK_ID"
  echo "This will ONLY delete notebooks matching: 'TEMP: {{package_name}} Media Generation'"
  read -p "Delete this temporary notebook? (y/N): " CONFIRM

  # Step 4: Delete only with explicit confirmation
  if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    if nlm notebook delete --id "$NOTEBOOK_ID" 2>/dev/null; then
      echo "✓ Deleted temporary notebook: $NOTEBOOK_ID"
    else
      echo "✗ Failed to delete notebook (may have been deleted already)"
      exit 1
    fi
  else
    echo "✗ Cleanup cancelled - notebook kept"
  fi
else
  echo "✓ No temporary notebooks found matching pattern"
fi
```

**Safety features**:
- **Confirmation prompt**: Requires explicit `y` before deletion
- **Pattern matching**: Only deletes notebooks with exact pattern match
- **Error handling**: Detects and reports deletion failures
- **Dry-run mode**: Shows what will be deleted before asking for confirmation

**⚠️  WARNING: Deletion is permanent**

**Before running cleanup**, verify:
1. **The notebook ID matches**: Check that `NOTEBOOK_ID` is the temporary notebook you just created
2. **No similar notebook names**: Ensure you don't have real notebooks with similar names
3. **Backup important data**: NotebookLM doesn't have undelete - export important notebooks first

**Risks mitigated by this approach**:
- ❌ **Overly broad grep pattern**: Fixed by exact pattern match + confirmation prompt
- ❌ **Silent failures**: Fixed by explicit error handling and exit codes
- ❌ **Wrong notebook deletion**: Fixed by dry-run mode + user confirmation
- ❌ **User confusion**: Fixed by clear "TEMP:" prefix + safety warnings

**Why use clearly named temp notebooks:**
- **Easy identification**: "TEMP: {package} Media Generation [timestamp]" makes it obvious these are temporary
- **Prevents clutter**: Don't leave generic "My Notebook" entries in your NotebookLM library
- **Safe cleanup**: Clear naming pattern ensures you only delete temp notebooks, not real ones
- **Debugging**: Timestamp helps identify which notebook belongs to which /package run

**Usage example - Typical cleanup session:**

```bash
# After running /package, you have a temporary notebook
# Let's clean it up

$ nlm notebook list
Notebooks:
abc123  TEMP: mylib Media Generation [20260310_131419]
def456  My Project Research
ghi789  Package Documentation

# Run the cleanup command
$ NOTEBOOK_ID=$(nlm notebook list | grep "TEMP: mylib Media Generation" | head -1 | awk '{print $1}')
$ echo "Current notebooks:"
$ nlm notebook list
Notebooks:
abc123  TEMP: mylib Media Generation [20260310_131419]
def456  My Project Research
ghi789  Package Documentation

$ echo "Found temporary notebook: abc123"
Found temporary notebook: abc123

$ echo "This will ONLY delete notebooks matching: 'TEMP: mylib Media Generation'"
This will ONLY delete notebooks matching: 'TEMP: mylib Media Generation'

$ read -p "Delete this temporary notebook? (y/N): " CONFIRM
Delete this temporary notebook? (y/N): y

$ if nlm notebook delete --id "abc123" 2>/dev/null; then
>   echo "✓ Deleted temporary notebook: abc123"
> else
>   echo "✗ Failed to delete notebook (may have been deleted already)"
>   exit 1
> fi
✓ Deleted temporary notebook: abc123

$ nlm notebook list
Notebooks:
def456  My Project Research
ghi789  Package Documentation
```

**Troubleshooting - Common cleanup issues:**

**Issue 1: "NOTEBOOK_ID is empty"**
- **Cause**: No notebooks match the pattern (already deleted or never created)
- **Solution**: This is expected - no cleanup needed
- **Verify**: Run `nlm notebook list` to see current notebooks

**Issue 2: "Pattern doesn't match"**
- **Cause**: Package name in grep pattern doesn't match actual notebook name
- **Solution**: Use broader pattern or manually select notebook ID from list
- **Example**: `grep "TEMP: mylib"` instead of `grep "TEMP: mylib Media Generation"`

**Issue 3: "Multiple notebooks match"**
- **Cause**: Multiple /package runs created temp notebooks
- **Solution**: Review list and decide which to delete, or delete all that match
- **Safe approach**: Run cleanup multiple times, confirm each deletion individually

**Issue 4: "Permission denied" or "Deletion fails"**
- **Cause**: NotebookLM authentication issue or network problem
- **Solution**:
  1. Check `nlm` CLI is authenticated: `nlm auth status`
  2. Re-authenticate if needed: `nlm login`
  3. Verify network connectivity
  4. Try manual deletion via NotebookLM web interface

**Quality comparison:**

| Approach | Source Material | Asset Quality | Time |
|----------|----------------|---------------|------|
| **Single README** | 1 file | Generic, shallow | Fast (~30s upload) |
| **Multi-source** | 10-50 files | Accurate, detailed, professional | Medium (~2min upload) |
| **Review bundle only** | 1 comprehensive file | Good architecture, missing implementation details | Fast (~30s upload) |
| **Review bundle + source files** | 1 architecture doc + 10-50 files | **Best quality** - context + implementation | Medium (~2min total) |

**Recommended strategy:**
1. **Default**: Review bundle + source files (production assets)
   - Review bundle provides architectural overview and design intent
   - Source files provide implementation details and concrete examples
   - Best of both worlds: high-level understanding + low-level evidence
2. **Fast iteration**: Review bundle only for testing /package workflow
3. **Fallback**: Multi-source without review bundle if review_bundle skill unavailable
3. **Fallback**: Single README if sources unavailable (degraded quality)

**Recommended video structure:**
```
CONTEXT (10-15s): Name the package and its purpose in one sentence.
WORKFLOW (25-40s): Show how it detects type, generates structure, and validates outputs.
ARTIFACTS (20-30s): Call out the key outputs: docs, CI/CD, flowchart, video, slides.
SUMMARY (10-15s): Close with the practical result for a developer using the package.
```

**Avoid this anti-pattern:**
- long “problem/pain/agitate” intros
- generic business narration
- theatrical transitions
- repeating the same feature list in multiple ways
- durations over 2 minutes unless the user explicitly wants a deep dive

**Why the old approach was annoying:**
- PBS tends to produce sales-demo narration rather than technical explanation
- fixed long sections bias NotebookLM toward overlong scripts
- `auto_select` style makes tone unpredictable
- the result often sounds generic even when the source material is technical

**Quality verification:**
- Check assets contain package name
- Verify relevance to package purpose
- Validate formats (banner: 1200×630 horizontal)
- Reject generic/wrong-format assets and retry

**Duration**: 5-10 minutes (depending on selected assets)

**Output**: Professional visual assets in `assets/` directory
- `assets/banners/{package}_banner.png`
- `assets/infographics/{package}_architecture.png`
- `assets/videos/{package}_explainer_pbs.mp4`
- `assets/slides/{package}_slides.pdf` (view and download as PDF)

**Rationale**: Media generation after code review ensures we're creating assets for quality code. Portfolio polish (PHASE 5) then references these visual assets in README.md.

---

## System Overview Diagrams (GitHub-First Mermaid)

**Objective**: Generate editable Mermaid architecture flowcharts that render cleanly on GitHub.

**When**: Runs automatically after NotebookLM media generation.

**What this does:**
- Creates plain Mermaid flowcharts for the README and optional supporting docs
- Generates a high-level system overview and workflow diagram
- Outputs source diagrams to `docs/diagrams/` for easy editing and git tracking
- Embeds the GitHub-safe overview directly in `README.md`

**GitHub compatibility rules (mandatory):**
- Target **GitHub's Mermaid renderer**, not Mermaid Live's broader feature set
- Prefer `graph TB` or `flowchart TB` system-overview diagrams for anything embedded in `README.md`
- Keep labels short and structural: phases, systems, outputs, decisions
- Do **not** use Mermaid C4 blocks (`C4Context`, `C4Container`, `C4Component`) in GitHub-facing README sections
- Do **not** emit `UpdateLayoutConfig(...)`, `include:`, or malformed init closers like `%%%`
- If technical C4 diagrams are still useful, keep them as optional secondary docs and verify they are not the primary README artifact

**Diagram types generated:**

| Diagram | Purpose | Output File | Style |
|---------|---------|-------------|-------|
| **System Overview** | High-level architecture and outputs | `docs/diagrams/system_overview.mmd` | Mermaid flowchart |
| **Workflow** | Phase-by-phase pipeline view | `docs/diagrams/workflow.mmd` | Mermaid flowchart |

**Why this style:**
- **Editable**: Text-based → easy to update alongside code
- **Version-controllable**: Track changes in git like code
- **Renderable**: GitHub renders basic Mermaid flowcharts more consistently than C4
- **Readable**: Better portfolio presentation for recruiters and repo visitors
- **Portable**: Same structure works in README, docs pages, and HTML wrappers

**Execution flow:**
```bash
# 1. Create diagrams directory
mkdir -p docs/diagrams

# 2. Generate GitHub-safe Mermaid flowcharts
# Prefer system_overview.mmd and workflow.mmd

# 3. Copy GitHub-compatible overview into README.md
```mermaid
graph TB
    Input[User: /{{package_name}}] --> Detect[Detect Package Type]
    Detect --> Type{Package Type?}
    Type -->|Plugin| Plugin[Plugin Structure]
    Type -->|Skill| Skill[Skill Structure]
    Type -->|Library| Library[Library Structure]
    Plugin --> Polish[Portfolio Polish]
    Skill --> Polish
    Library --> Polish
    Polish --> Docs[Documentation]
    Polish --> Media[Media Assets]
    Polish --> CI[CI/CD]
    Docs --> Output[GitHub-Ready Package]
    Media --> Output
    CI --> Output
```
```

**Duration**: ~1 minute (both flowcharts)

**Auto-skip conditions:**
- Mermaid diagrams already exist in `docs/diagrams/`
- User explicitly opts out with `--skip mermaid`

**Provider requirements:**
- **mermaid-diagrams skill**: Installed via `/universal-skills-manager` or ClawHub
- No API keys required (pure Mermaid syntax generation)

**Quality verification:**
- Check the README diagram is a plain Mermaid flowchart, not C4
- Verify relationships show the major phases, decisions, and outputs
- Validate Mermaid syntax renders correctly
- Scan `README.md` and `docs/diagrams/*.mmd` for banned patterns before finishing:
  - `C4Context`
  - `C4Container`
  - `C4Component`
  - `System_Bnd`
  - `Container_Bnd`
  - `Component_Bnd`
  - `UpdateLayoutConfig`
  - `include:`
  - `%%%`

**Comparison: Mermaid vs NotebookLM diagrams**

| Aspect | Mermaid Diagrams | NotebookLM Diagrams |
|--------|-----------------|---------------------|
| **Format** | Text (`.mmd` files) | Images (`.png`) |
| **Version control** | ✅ Git-diff friendly | ❌ Binary changes |
| **Editability** | ✅ Text editor | ❌ Regenerate only |
| **Renderers** | GitHub, VS Code, Mermaid Live | Image viewers |
| **Best for** | Technical documentation, architecture specs | Social preview, quick visuals |
| **Location** | `docs/diagrams/` | `assets/infographics/` |
| **Automation** | Auto-generated in /package | Auto-generated in /package |

**Both are generated automatically** by `/package` - each serves a different purpose.

---

## GitHub Pages Video Player

**Objective**: Generate a single-purpose HTML page for browser playback of the explainer video.

**When**: Runs after the explainer video is generated.

**What this does:**
- Creates `docs/video.html` as a lightweight HTML5 player page
- Keeps GitHub Pages focused on playback only
- Leaves architecture and workflow explanation on the main GitHub repository page

**Generated asset:**

| Asset | Purpose | Format | Output |
|-------|---------|--------|--------|
| **Video player page** | Browser playback for the README video link | HTML | `docs/video.html` |

**Integration with README.md:**

```markdown
[![Watch the demo with audio](assets/videos/{{package_name}}_video_poster.png)](https://{{github_username}}.github.io/{{package_name}}/docs/video.html)
```

**Rules:**
- Do not create extra GitHub Pages docs for architecture or workflow unless the user explicitly asks for a separate docs site
- Keep GitHub as the source of truth for technical documentation
- Use GitHub Pages only to solve the inline video playback limitation

---

## Code Flow Diagrams (On-Demand)

**For function-level visualization**, use `/code-flow-visualizer` separately:

```bash
# Visualize a specific function
/code-flow-visualizer path/to/file.py function_name

# Auto-detect main functions
/code-flow-visualizer path/to/file.py
```

**When to use:**
- Documenting complex algorithm logic
- Explaining code flow in pull requests
- Creating onboarding diagrams for new contributors
- Analyzing unfamiliar codebases

**Output:** Mermaid flowchart showing conditional branches, loops, and data flow

**Note:** Not automatically invoked by `/package` - use on-demand for specific files.

---

## GitHub Slide Deck Integration

**PDF Usage:**

| Format | Best For | GitHub Integration |
|--------|----------|-------------------|
| **PDF** | Primary viewing format on GitHub | `[View Slides (PDF)](assets/slides/{package}_slides.pdf)` |

**Recommended approach:**
1. Keep the published slide deck in `assets/slides/` as PDF
2. Make the PDF the first and most prominent slide link in `README.md`
3. Use a slide preview image that links directly to the PDF
4. Prefer this README pattern:
   `View Slides (PDF)`, then `Download PDF`

---

## PHASE 5: Portfolio Polish (Auto-invoked after creation)

**Objective**: Transform package into portfolio-quality GitHub artifact.

**Trigger**: Automatically invoked after PHASE 4 unless `--no-polish` flag is set.

**Workflow**: DETECT → ANALYZE → GENERATE → VALIDATE → REPORT

**Auto-generated artifacts** (if missing):

- **Badges**: Coverage, version, license, CI status (shields.io)
- **CI/CD**: GitHub Actions workflows for testing and deployment
- **Documentation**: CHANGELOG.md, CONTRIBUTING.md, AGENTS.md, API docs from docstrings
- **Architecture flowchart**: GitHub-safe Mermaid flowchart in README.md
- **Video playback page**: `docs/video.html` linked from README for GitHub Pages playback
- **Quick Start**: Installation and usage examples for < 5min setup

**CI/CD Workflow Template** (`.github/workflows/test.yml`):

```yaml
name: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.14'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov

    - name: Run tests
      run: |
        pytest tests/ -v --cov=core --cov-report=term
```

**IMPORTANT:**
- ❌ **NO Codecov integration** - Do NOT upload coverage to external services
- ✅ Local coverage reporting only (--cov-report=term)
- ✅ CI badge should show workflow status, not external coverage service

**Checks performed**:
- Platform compatibility (Windows docs vs .sh scripts in hook configs)
- MCP server structure and dependencies
- Security: No secrets in git (.env, *.key, credentials)
- Test coverage reporting and badges

**Output**: Portfolio-ready repository with badges, CI/CD, docs, and examples.
## PHASE 6: Cleanup (Auto-invoked)**Objective**: Detect and remove obsolete files after refactoring/scaffolding.**When**: Automatically runs after PHASE 5 (Portfolio Polish) completes.**What this detects**:- **Backup files** (*.backup-*, *.old, *.bak) - Shows file size and removal command- **Orphaned test files** - Tests for modules that no longer exist- **Obsolete documentation** - Old CHANGELOGs, phase completion docs, verification docs- **Duplicate implementations** - Known refactoring patterns (e.g., skill_enforcement → skill_first_gate)**Output**: `CLEANUP_REPORT.md` with:- Categorized list of files to remove- Evidence for why each should be removed- Bulk removal commands ready to run- Commit message template**Usage**: Review report and manually remove files (recommended for first run).
## PHASE 7: Git Ready (Auto-invoked)**Objective**: Initialize git repository and create initial commit.**When**: Automatically runs after PHASE 4 (Validate) completes.**What this does**:- Initialize git repository (if not already a git repo): `git init`- Add all files and create initial commit: `git commit -m "Initial commit: Package scaffold..."`- Set main branch: `git branch -M main`- Skips if `.git/` directory already exists**Manual steps** (user does when ready):- Add remote: `git remote add origin https://github.com/{{USERNAME}}/{{NAME}}.git`- Push to GitHub: `git push -u origin main`## PHASE 7: Recruiter Readiness Validation (Auto-invoked)**Objective**: Validate package is showcase-ready for recruiters before GitHub posting.**When**: Automatically runs after PHASE 5 (Portfolio Polish) completes.**Checks performed**:- TODO comments in pyproject.toml (suggests incomplete work)- Plan files in root (looks messy/unprofessional)- Missing CI/CD workflow (reduces perceived professionalism)- No tests directory (lack of quality evidence)- Version is 0.0.x or 0.1.x (suggests experimental/unstable)**Scoring**: 90-100 (Excellent), 70-89 (Good), 50-69 (Fair), <50 (Poor)**Auto-fixes available**: Remove TODOs, move plan files to docs/planning/, create CI/CD workflow, bump version to 0.5.0 or 1.0.0.**Output**: `RECRUITER_READINESS_REPORT.md` with score, issues found, and one-command fixes.

## Integration

**Related skills:**
- `/init` - Initialize CLAUDE.md for new projects
- `/github-public-posting` - Pre-publish checklist for GitHub

**Deprecated skills:**
- `/media-pipeline` - Functionality merged into `/package` as PHASE 4.7 (Media Generation)

**Used by:**
- **PRIMARY**: Claude Code Plugins (hooks, skills, MCP integration)
- **MIGRATION**: Python libraries being converted to plugins
- **ADVANCED**: Pure Python backend libraries (no Claude Code integration)

---

## COMPLETION REPORT (Always Show at End)

**MANDATORY**: After ALL phases complete, show GitHub readiness status.

### What to Check

```bash
# 1. Check if GitHub remote exists
git remote -v | grep github.com

# 2. Check if repo is public (requires gh CLI)
gh repo view --json name,owner,isPublic,url

# 3. Verify portfolio polish completeness
checklist=(
  "README.md with badges"
  "CHANGELOG.md"
  "CONTRIBUTING.md"
  "AGENTS.md"
  ".github/workflows/test.yml"
  "LICENSE file"
  "tests/ directory exists"
  "pytest tests pass"
  "pyproject.toml or setup.py"
  "Media assets generated (if applicable)"
)
```

### Output Format

**MUST show one of these statuses:**

#### ✅ STATUS: PUBLIC ON GITHUB
```
🎉 Package is LIVE and PUBLIC on GitHub!

🔗 https://github.com/EndUser123/package-name

✅ Portfolio polish: COMPLETE
✅ All tests: PASSING
✅ CI/CD: CONFIGURED
✅ Documentation: COMPLETE
✅ Media assets: GENERATED
✅ Ready for: recruiters, portfolio, public use
```

#### ⚠️ STATUS: READY FOR GITHUB (NOT YET PUBLIC)
```
✅ Package is POLISHED and ready for GitHub!

📋 Ready to publish:
- All badges, CI/CD, docs complete
- Tests passing, coverage configured
- Media assets generated
- CHANGELOG and CONTRIBUTING docs ready

⚠️ Next steps:
1. Create GitHub repo: gh repo create package-name --public --source=. --push
2. Or manually: git remote add origin https://github.com/USER/REPO.git && git push -u origin main

🔗 After pushing: https://github.com/YOUR_USERNAME/package-name
```

#### 🔄 STATUS: LOCAL ONLY (NEEDS POLISH)
```
📦 Package exists locally

⚠️ Not yet ready for GitHub:
- [ ] Complete portfolio polish (PHASE 5)
- [ ] Generate media assets (PHASE 4.7)
- [ ] Ensure all tests pass
- [ ] Review Recruiter Readiness Report

💡 Run: /github-ready <package-path> --polish
```

## Changelog

### v5.6.0 (2026-03-14)
- ✅ **PLUGIN STANDARDS VALIDATION**: Added PHASE 1.7 - automatic validation of plugin files/folders against Claude Code plugin standards
- ✅ **CRUD RECOMMENDATIONS**: Auto-detects non-standard files and provides Create/Update/Delete recommendations
- ✅ **MULTI-PLUGIN VALIDATION**: Standards validated against multiple production plugins (handoff, search-research, github-ready)
- ✅ **AUTO-CLEANUP**: One-command cleanup script for removing/moving non-standard files
- ✅ **FORBIDDEN FILE DETECTION**: Identifies `pyproject.toml`, `src/`, `setup.py` violations in plugins
- ✅ **TEMPORARY FILE DETECTION**: Finds test scripts, diagnostic artifacts, temporary documentation
- ✅ **COMPLIANCE SCORING**: Generates compliance scores (0-100) with detailed violation reports
- ✅ **WORKFLOW INTEGRATION**: Added `validate_plugin_standards` to workflow_steps
- ✅ **STANDARDS SOURCE**: Validated against official Claude Code plugin documentation + 3 production plugins

### v5.5.5 (2026-03-10)
- ✅ **GITHUB-COMPATIBLE MEDIA**: Fixed README media template for GitHub compatibility
- ✅ Replaced inline README video attempts with GitHub-safe links
- ✅ Removed broken PDF thumbnail images - use clean markdown links instead
- ✅ Added shields.io badges for visual appeal (🎬 Watch Video, 🎙️ Listen Now)
- ✅ Simplified PDF links - open in GitHub's built-in PDF viewer
- ✅ Documentation updated: "No HTML tags in README - GitHub markdown is safer"

### v5.5.4 (2026-03-10)
- ✅ **MEDIA ASSETS TEMPLATE**: Added Media Assets section template to PHASE 3 README generation
- ✅ Early media template for browser playback experiments
- ✅ Center-aligned media with proper markdown image embedding
- ✅ Download links and direct links for all assets
- ✅ Improved media visibility on GitHub with direct links and better structure
- ✅ Images embedded directly, PDFs with GitHub viewer integration

### v5.5.6 (2026-03-11)
- ✅ **GITHUB PAGES VIDEO PLAYBACK**: README now links preview GIFs to `docs/video.html` on GitHub Pages
- ✅ README architecture section now defaults to GitHub-safe Mermaid flowcharts instead of C4 blocks
- ✅ Media guidance updated to treat direct MP4 links as fallback, not the primary playback path
- ✅ Skill instructions aligned with the working `github.io` player-page workflow

### v5.5.3 (2026-03-10)
- ✅ **COMPLETION REPORT**: Added GitHub readiness status check at end of workflow
- ✅ Always shows if package is public on GitHub.com
- ✅ Indicates if package is ready for GitHub (perfect polish)
- ✅ Shows what's missing if not yet ready
- ✅ Three clear statuses: PUBLIC, READY FOR GITHUB, LOCAL ONLY

### v5.5.2 (2026-03-10)
- ✅ **CI/CD TEMPLATE**: Added explicit GitHub Actions workflow template to PHASE 5
- ✅ **NO CODECOV**: Clarified that CI workflows should NOT upload to external coverage services
- ✅ Coverage reporting: Local terminal output only (--cov-report=term)
- ✅ Prevents confusion about Codecov integration - no external service uploads

### v5.5.1 (2026-03-10)
- ✅ **DOCUMENTATION**: Added comprehensive "Three Deployment Models" template to PHASE 3
- ✅ README templates now include SKILLS/HOOKS/PLUGINS deployment comparison table
- ✅ Added "Common Mistakes to Avoid" section preventing deployment confusion
- ✅ Added "Which Model Should You Use?" decision guide for developers
- ✅ Auto-generated READMEs now prevent dev mode setup confusion
- ✅ No more manual explanation needed - skill creates complete deployment docs

### v5.4.3 (2026-03-10)
- ✅ **DOCUMENTATION**: Added comprehensive usage examples for NotebookLM cleanup
- ✅ Added step-by-step example session showing typical cleanup workflow
- ✅ Added troubleshooting section with 4 common issues and solutions
- ✅ Documented edge cases: empty NOTEBOOK_ID, pattern mismatches, multiple matches, permission errors
- ✅ Improved user onboarding with realistic command examples
- ✅ Operational verification tests passed - all safety features validated

### v5.4.2 (2026-03-10)
- ✅ **SECURITY FIX**: Added defensive error handling to NotebookLM cleanup
- ✅ Confirmation prompt required before deletion (prevents accidental data loss)
- ✅ Error detection and reporting for failed deletion attempts
- ✅ Dry-run mode shows what will be deleted before asking confirmation
- ✅ Safety warnings about permanent deletion and verification steps
- ✅ Fixed risk: Overly broad grep pattern now has explicit confirmation
- ✅ Fixed risk: Silent failures now detected and reported
- ✅ Pre-mortem validated approach through operational verification

### v5.4.1 (2026-03-10)
- ✅ **UPDATED**: NotebookLM temporary notebooks now use clear naming pattern
- ✅ Temp notebooks named: "TEMP: {package} Media Generation [timestamp]"
- ✅ Added notebook cleanup instructions after asset generation
- ✅ Prevents clutter in NotebookLM library with clearly identifiable temporary notebooks
- ✅ Safe cleanup pattern ensures only temp notebooks are deleted

### v5.4.0 (2026-03-09)
- ✅ **MERGED**: /media-pipeline integrated as PHASE 4.7 (Media Generation)
- ✅ Auto-generates professional portfolio assets (banners, diagrams, videos)
- ✅ NotebookLM integration for architecture diagrams and explainer videos
- ✅ Initial explainer video structure for AI narrated overviews (later refined toward a shorter technical style)
- ✅ Vision API verification for asset quality before acceptance
- ✅ Provider detection (NotebookLM, OpenRouter) with clear setup instructions
- ✅ Auto-skip for internal tools (python-library type) or when providers missing
- ✅ `--skip media` flag for fast iterations without visual asset generation
- ✅ **DEPRECATED**: Standalone /media-pipeline skill (functionality moved to /package)
- ✅ Unified workflow: one command creates structure, validates code, generates media, polishes portfolio

### v5.5.0 (2026-03-10)
- ✅ Integrated meta-review system into PHASE 4.5 (T-007)
- ✅ Added cross-file analysis: path_traversal, import_graph, doc_consistency
- ✅ Combined code-review plugin + meta-review for comprehensive validation
- ✅ AnalysisUnit-based manifest-driven review workflow
- ✅ Optional meta-review via META_REVIEW_ENABLED env var (default: true)
- ✅ See test_meta_review_integration.py for full integration tests
- ✅ No breaking changes to existing workflows

### v5.3.0 (2026-03-07)
- ✅ Added PHASE 4.5: Code Review (code-review plugin integration)
- ✅ Automated quality validation before portfolio polish
- ✅ Confidence-based scoring (80+ threshold) for findings
- ✅ Reviews package structure, configuration, and code
- ✅ Prevents polishing code with quality issues
- ✅ More efficient workflow: fix before polishing
- ✅ See skill_review_comprehensive_analysis.md for full integration details

### v5.2.0 (2025-03-07)
- ✅ Updated to Claude Code plugin best practices (v5.2 structure)
- ✅ Added `core/` directory for Python code
- ✅ Added `hooks/hooks.json` for hook configuration
- ✅ Added `.mcp.json` for MCP server configuration
- ✅ Removed `pyproject.toml` (plugins don't need pip packaging)
- ✅ Added local development setup (junctions/symlinks)
- ✅ Added brownfield conversion workflow (src/ → core/)
- ✅ Enhanced progressive disclosure with references/
- ✅ Reduced word count from 10,996 to ~4,000 words
- ✅ Added Bundled Resources documentation
- ✅ Fixed integration verification (removed //p-2025)
- ✅ Simplified PHASE sections with concise references

### v5.1.0
- Initial router-based hook package support
- MCP server directory structure
- pyproject.toml packaging

### v5.0.0
- Python library scaffolding
- Claude skill creation
- Badge generation
- CI/CD workflows

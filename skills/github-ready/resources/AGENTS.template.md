# AGENTS.md

> AI-maintainable documentation for the {{package_name}} package. This file provides context and constraints for AI assistants (Claude, Copilot, etc.) working on this codebase.

## Package Overview

**{{package_name}}** is a {{package_type}} that {{one_sentence_description}}.

**Architecture**: {{architecture_summary}}

**Key Constraints**:
- {{constraint_1}}
- {{constraint_2}}
- {{constraint_3}}

## Directory Structure

```
{{package_name}}/
├── .claude-plugin/         # Plugin metadata (plugin.json)
├── core/                   # Python source code (authoritative)
│   ├── hooks/             # Hook entry points (if applicable)
│   ├── backends/          # Backend implementations (if applicable)
│   ├── utils/             # Utility modules
│   └── tests/             # Unit tests for core modules
├── hooks/                 # Hook configuration (hooks.json)
├── tests/                 # Integration and feature tests
├── examples/              # Usage examples
├── docs/                  # Additional documentation
├── assets/                # Media assets (badges, videos, diagrams)
├── .github/workflows/     # CI/CD workflows
├── README.md              # Package overview
├── CHANGELOG.md           # Version history
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE                # MIT license
└── AGENTS.md              # This file
```

## Development Setup

### Local Development

{{local_dev_instructions}}

### Running Tests

```bash
# Quick test
pytest P:/packages/{{package_name}}/tests/ -q

# With coverage
pytest P:/packages/{{package_name}}/tests/ --cov=core --cov-report=term-missing
```

## Key Implementation Details

{{implementation_notes}}

## Common Tasks

{{common_tasks}}

## Architecture Decisions

{{architecture_decisions}}

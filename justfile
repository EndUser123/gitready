# github-ready Automation Commands
# https://github.com/casey/just

# Master command to sync, update, and regenerate everything
polish: sync diagrams nlm-update nlm-media publish-media
    @echo "✅ Project is now GitHub-ready and portfolio-polished."

# Synchronize version across core, plugin.json, and README
sync:
    python core/sync.py

# Placeholder for Mermaid CLI if you want to export PNGs locally
diagrams:
    @echo "Verifying C4 Mermaid diagrams in docs/diagrams/..."
    # If mmdc is installed: mmdc -i docs/diagrams/c4_context.mmd -o assets/c4_context.png

# Update NotebookLM sources with the latest code and skills
nlm-update:
    nlm source add --file core/main.py \
                   --file core/__init__.py \
                   --file core/sync.py \
                   --file .claude-plugin/plugin.json \
                   --file README.md \
                   --file AGENTS.md \
                   --file P:/.claude/skills/package/SKILL.md

# Regenerate high-fidelity portfolio assets
nlm-media:
    nlm video create --notebook "TEMP: github-ready Media Generation" --output assets/explainer.mp4
    nlm slides create --notebook "TEMP: github-ready Media Generation" --format detailed_deck --output assets/slides.pdf
    nlm infographic create --notebook "TEMP: github-ready Media Generation" --output assets/infographic.png

# Upload local assets to GitHub Releases and update README links
publish-media:
    # Create a "media" release if it doesn't exist, then upload the video
    gh release create media --title "Project Media Assets" --notes "Automated uploads" || true
    gh release upload media assets/explainer.mp4 --clobber
    gh release upload media assets/slides.pdf --clobber
    gh release upload media/assets/infographic.png --clobber
    @echo "✅ Media uploaded to GitHub Releases"
    # Note: README will need manual update with new release URLs

# Quick validation before committing
validate: sync
    @echo "Running pre-commit validation..."
    python core/sync.py
    ruff check core/
    pytest tests/ -q
    @echo "✅ All validations passed"

# Full release checklist
release: polish validate
    @echo "✅ Ready for release! Don't forget to:"
    @echo "  1. Update README with new release URLs"
    @echo "  2. Commit changes: git add . && git commit -m 'chore: polish v$(python -c 'import core; print(core.__version__)')'"
    @echo "  3. Create git tag: git tag v$(python -c 'import core; print(core.__version__)')"
    @echo "  4. Push to GitHub: git push && git push --tags"

# Development workflow (fast iteration)
dev:
    @echo "🚀 Quick development setup..."
    python -m pip install -q pytest ruff mypy 2>/dev/null || true
    @echo "✅ Dev environment ready"

# Clean up generated files
clean:
    @echo "🧹 Cleaning up temporary files..."
    rm -rf .pytest_cache .ruff_cache __pycache__
    rm -f *.pyc
    @echo "✅ Cleanup complete"

# Show current version
version:
    @echo "github-ready v$(python -c 'import core; print(core.__version__)')"

# Run full test suite with coverage
test:
    pytest tests/ -v --cov=core --cov-report=term-mvv

# Lint code
lint:
    ruff check core/
    ruff format --check core/

# Auto-fix linting issues
fix:
    ruff check --fix core/
    ruff format core/

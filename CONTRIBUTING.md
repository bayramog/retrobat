# Contributing to RetroBat macOS Fork

## Fork Policy

This is a **fork-focused project** for macOS support. We are NOT accepting contributions back to upstream until validation goals are met.

## Before Contributing

1. Read all documentation in `docs/macos/`
2. Install git hooks: `./tools/dev/install-git-hooks.sh`
3. Understand the [branching policy](docs/macos/BRANCHING_POLICY.md)
4. Review [role decisions](docs/macos/ROLE_DECISIONS.md)

## Development Workflow

See [LOCAL_WORKFLOW.md](docs/macos/LOCAL_WORKFLOW.md) for detailed setup.

### Quick Start
```bash
# Install git hooks
./tools/dev/install-git-hooks.sh

# Create feature branch
git checkout -b feat/your-feature

# Make changes, commit, push
git push origin feat/your-feature
```

## Pull Request Process

1. **Target Branch**: PRs should target `main` (after quality gates pass)
2. **Template**: Fill out the entire PR template
3. **Tests**: Ensure validation criteria pass
4. **Review**: Wait for maintainer review
5. **No Force Push**: After review starts

## Code Standards

- Follow existing code style
- Add comments for complex logic
- Keep commits atomic and well-described
- No merge commits (rebase preferred)

## macOS-Specific Guidelines

- **Apple Silicon Only**: No Intel support
- **Native**: Prefer native solutions over emulation
- **Security**: Respect macOS security features (Gatekeeper, code signing)
- **Testing**: Test on actual Apple Silicon hardware

## Issue Reporting

- Use issue templates
- Provide system information
- Include reproduction steps
- Attach logs when applicable

## Questions?

Ask in discussions or issues, not in PRs.

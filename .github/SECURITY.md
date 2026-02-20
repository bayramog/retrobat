# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| dev/*   | :x:                |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability:

1. **DO NOT** open a public GitHub issue
2. Email the maintainer directly at: bayramog@users.noreply.github.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## Security Practices

### Code Review
- All PRs require review before merge
- No direct pushes to main branch
- Fork-level changes only until validation complete

### Dependencies
- Regular dependency audits
- No unverified third-party scripts
- Submodules pinned to specific commits

### Secrets Management
- No credentials in repository
- No API keys in code
- Use environment variables for sensitive data

### macOS Security
- Code signing required for releases
- Gatekeeper compatibility mandatory
- Apple Silicon security features respected

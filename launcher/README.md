# RetroBat Launcher - macOS Edition

Python-based emulator launcher for RetroBat on macOS (Apple Silicon).

## Project Structure

```
launcher/
├── __init__.py          # Package initialization
├── __main__.py          # Main entry point
├── setup.py             # Package setup configuration
├── requirements.txt     # Runtime dependencies
├── requirements-dev.txt # Development dependencies
├── cli/                 # Command-line interface
│   └── __init__.py
├── platform/            # Platform abstraction layer
│   └── __init__.py
├── config/              # Configuration management
│   └── __init__.py
├── emulators/           # Emulator generators
│   └── __init__.py
└── utils/               # Utility functions
    └── __init__.py
```

## Installation

```bash
# Install runtime dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in development mode
pip install -e .
```

## Usage

```bash
# Run as module
python -m launcher --help

# Or after installation
retrobat-launcher --help
```

## Development Status

🚧 **Alpha** - Under active development

Current implementation status:
- [x] Project structure
- [ ] CLI interface
- [ ] Platform abstraction
- [ ] Base generator
- [ ] RetroArch generator
- [ ] Configuration loader
- [ ] Factory pattern
- [ ] Main integration
- [ ] Unit tests
- [ ] E2E testing

## Requirements

- Python 3.11 or higher
- macOS (Apple Silicon)
- RetroArch (for testing)

## Documentation

See `/docs/research/` for detailed architecture and implementation documentation.

## License

LGPL v3 - See LICENSE file for details

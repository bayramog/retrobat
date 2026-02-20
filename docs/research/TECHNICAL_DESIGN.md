# macOS Launcher Technical Design

**Date:** 2026-02-20  
**Purpose:** Detailed technical design for macOS emulator launcher system

---

## 1. Overview

### 1.1 Objective
Create a Python-based emulator launcher for macOS that replaces `emulatorLauncher.exe` while maintaining compatibility with RetroBat's configuration system.

### 1.2 Design Principles
1. **Platform Abstraction:** OS-agnostic core with platform-specific adapters
2. **Extensibility:** Easy to add new emulators
3. **Maintainability:** Clear architecture, good documentation
4. **Testing:** Comprehensive unit and integration tests
5. **Compatibility:** Reuse existing RetroBat configurations

---

## 2. Architecture

### 2.1 Module Structure

```
launcher/
├── main.py                  # Entry point
├── cli/
│   └── parser.py            # Argument parsing
├── platform/
│   ├── base.py              # Base platform interface
│   └── macos.py             # macOS implementation
├── config/
│   ├── loader.py            # Load configurations
│   └── parser.py            # Parse configs
├── emulators/
│   ├── base.py              # Base emulator class
│   ├── factory.py           # Emulator factory
│   ├── retroarch.py         # RetroArch launcher
│   └── ...
└── utils/
    ├── logger.py            # Logging
    └── paths.py             # Path utilities
```

---

## 3. Core Components

### 3.1 Entry Point

```python
#!/usr/bin/env python3
def main():
    # Parse arguments
    args = ArgumentParser().parse()
    
    # Load configuration
    config = ConfigLoader()
    
    # Create emulator instance
    emulator = EmulatorFactory().create(args)
    
    # Launch emulator
    exit_code = emulator.launch()
    sys.exit(exit_code)
```

### 3.2 Platform Abstraction

```python
class PlatformBase(ABC):
    @abstractmethod
    def get_emulator_path(self, name: str) -> Path
    
    @abstractmethod
    def normalize_path(self, path: str) -> Path
```

### 3.3 Emulator Base Class

```python
class BaseEmulator(ABC):
    @abstractmethod
    def build_command(self) -> List[str]
    
    def launch(self) -> int:
        command = self.build_command()
        process = subprocess.Popen(command)
        return process.wait()
```

---

## 4. Implementation Phases

### Phase 1: MVP (Week 1-2)
- [ ] Basic CLI interface
- [ ] Platform detection
- [ ] RetroArch launcher only
- [ ] Config loader

### Phase 2: Expansion (Week 3-4)
- [ ] Add more emulators
- [ ] Complete config system
- [ ] Error handling

### Phase 3: Polish (Week 5-6)
- [ ] Tests
- [ ] Documentation
- [ ] Package for distribution

---

**Status:** Draft - Ready for Implementation

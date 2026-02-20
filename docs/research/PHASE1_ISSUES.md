# Phase 1 Implementation Issues

**Purpose:** GitHub issues for Phase 1 MVP implementation  
**Timeline:** 3-4 weeks  
**Goal:** Launch NES game via RetroArch on macOS

---

## Issue #1: Set Up Python Project Structure

**Title:** `feat(launcher): set up Python project structure for macOS launcher`

**Labels:** `enhancement`, `phase-1`, `infrastructure`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P0 - Critical

### Description
Create the foundational Python project structure for the macOS emulator launcher system.

### Tasks
- [ ] Create `launcher/` directory in repository root
- [ ] Set up Python package structure with `__init__.py` files
- [ ] Create module directories: `cli/`, `platform/`, `config/`, `emulators/`, `utils/`
- [ ] Create `requirements.txt` with dependencies
- [ ] Create `requirements-dev.txt` for development dependencies
- [ ] Create `setup.py` for package installation
- [ ] Add `.python-version` file (Python 3.11)
- [ ] Create basic `README.md` in `launcher/` directory
- [ ] Set up `.gitignore` for Python artifacts

### File Structure
```
launcher/
├── __init__.py
├── __main__.py
├── cli/
│   ├── __init__.py
│   └── parser.py
├── platform/
│   ├── __init__.py
│   ├── base.py
│   └── macos.py
├── config/
│   ├── __init__.py
│   └── loader.py
├── emulators/
│   ├── __init__.py
│   ├── base.py
│   └── factory.py
└── utils/
    ├── __init__.py
    ├── logger.py
    └── paths.py
```

### Dependencies
```python
# requirements.txt
PyYAML>=6.0
lxml>=4.9.0
psutil>=5.9.0

# requirements-dev.txt
pytest>=7.4.0
black>=23.0.0
pylint>=2.17.0
mypy>=1.4.0
```

### Acceptance Criteria
- [ ] All directories and `__init__.py` files created
- [ ] Dependencies installable with `pip install -r requirements.txt`
- [ ] Can import launcher package: `python -c "import launcher"`
- [ ] Black/pylint configured and passing
- [ ] README.md documents project structure

### Estimated Effort
1-2 days

---

## Issue #2: Implement Core CLI Interface

**Title:** `feat(launcher): implement command-line argument parser`

**Labels:** `enhancement`, `phase-1`, `cli`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P0 - Critical

### Description
Implement the command-line interface that parses arguments from EmulationStation, matching the functionality of `emulatorLauncher.exe`.

### Tasks
- [ ] Implement `cli/parser.py` with argparse
- [ ] Add required arguments: `-system`, `-emulator`, `-rom`
- [ ] Add optional arguments: `-core`, `-gameinfo`, `--controllers-config`
- [ ] Add debug flag: `--debug`, `--verbose`
- [ ] Implement argument validation
- [ ] Add help text and usage examples
- [ ] Create `__main__.py` entry point
- [ ] Add version information (`--version`)

### Command-Line Format
```bash
python -m launcher \
  -system nes \
  -emulator retroarch \
  -core mesen \
  -rom "/path/to/game.nes" \
  --debug
```

### Code Example
```python
# cli/parser.py
import argparse

class ArgumentParser:
    def parse(self):
        parser = argparse.ArgumentParser(
            description='RetroBat Emulator Launcher - macOS Edition'
        )
        parser.add_argument('-system', required=True, help='System name')
        parser.add_argument('-emulator', required=True, help='Emulator name')
        parser.add_argument('-core', help='Emulator core (for libretro)')
        parser.add_argument('-rom', required=True, help='ROM file path')
        parser.add_argument('-gameinfo', help='Game metadata XML')
        parser.add_argument('--controllers-config', help='Controllers config')
        parser.add_argument('--debug', action='store_true', help='Debug mode')
        parser.add_argument('--version', action='version', version='1.0.0')
        return parser.parse_args()
```

### Acceptance Criteria
- [ ] All required arguments parsed correctly
- [ ] Help text displays properly (`python -m launcher --help`)
- [ ] Invalid arguments show clear error messages
- [ ] Debug flag enables verbose logging
- [ ] Entry point works: `python -m launcher --version`

### Testing
```python
# Test command
python -m launcher \
  -system nes \
  -emulator retroarch \
  -core mesen \
  -rom test.nes \
  --debug
```

### Estimated Effort
1-2 days

---

## Issue #3: Implement Platform Abstraction Layer

**Title:** `feat(platform): implement macOS platform abstraction layer`

**Labels:** `enhancement`, `phase-1`, `platform`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P0 - Critical

### Description
Create the platform abstraction layer that handles macOS-specific operations like path normalization, emulator discovery, and process management.

### Tasks
- [ ] Implement `platform/base.py` - Abstract base class
- [ ] Implement `platform/macos.py` - macOS-specific implementation
- [ ] Add emulator path discovery (check common locations)
- [ ] Add path normalization (Windows → macOS)
- [ ] Add config directory resolution
- [ ] Add home directory resolution
- [ ] Implement process launching wrapper
- [ ] Add platform detection utility

### Code Structure
```python
# platform/base.py
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

class PlatformBase(ABC):
    @abstractmethod
    def get_emulator_path(self, emulator_name: str) -> Path:
        """Locate emulator executable"""
        pass
    
    @abstractmethod
    def get_config_dir(self) -> Path:
        """Get platform config directory"""
        pass
    
    @abstractmethod
    def normalize_path(self, path: str) -> Path:
        """Convert platform paths"""
        pass

# platform/macos.py
class MacOSPlatform(PlatformBase):
    def get_emulator_path(self, emulator_name: str) -> Path:
        locations = [
            Path('/Applications') / f'{emulator_name}.app/Contents/MacOS/{emulator_name}',
            Path.home() / 'Applications' / f'{emulator_name}.app/Contents/MacOS/{emulator_name}',
            Path('/usr/local/bin') / emulator_name,
            Path('/opt/homebrew/bin') / emulator_name,
        ]
        for loc in locations:
            if loc.exists():
                return loc
        raise FileNotFoundError(f"{emulator_name} not found")
    
    def get_config_dir(self) -> Path:
        return Path.home() / 'Library/Application Support/RetroBat'
    
    def normalize_path(self, path: str) -> Path:
        # Convert Windows paths to macOS
        path = path.replace('\\', '/')
        path = re.sub(r'^[A-Z]:', '', path)
        return Path(path).expanduser()
```

### Emulator Discovery Locations
```
/Applications/RetroArch.app/Contents/MacOS/RetroArch
/Applications/PPSSPP.app/Contents/MacOS/PPSSPP
~/Applications/*.app
/usr/local/bin/*
/opt/homebrew/bin/*
```

### Acceptance Criteria
- [ ] Can detect RetroArch installation
- [ ] Path normalization handles Windows paths
- [ ] Config directory created if not exists
- [ ] Raises clear errors when emulator not found
- [ ] Unit tests cover all methods

### Testing
```python
# Test platform detection
platform = MacOSPlatform()
retroarch = platform.get_emulator_path('retroarch')
assert retroarch.exists()

# Test path normalization
windows_path = 'C:\\RetroBat\\roms\\nes\\game.nes'
macos_path = platform.normalize_path(windows_path)
assert str(macos_path) == '/RetroBat/roms/nes/game.nes'
```

### Estimated Effort
2-3 days

---

## Issue #4: Implement Base Generator Class

**Title:** `feat(emulators): implement base generator class`

**Labels:** `enhancement`, `phase-1`, `core`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P0 - Critical

### Description
Create the base generator class that all emulator-specific generators will inherit from. This mirrors the C# `Generator` base class from `emulatorLauncher`.

### Tasks
- [ ] Implement `emulators/base.py` - Abstract base generator
- [ ] Add abstract methods: `build_command()`, `configure()`
- [ ] Implement common methods: `launch()`, `terminate()`
- [ ] Add logging support
- [ ] Add error handling
- [ ] Implement process lifecycle management
- [ ] Add exit code handling

### Code Structure
```python
# emulators/base.py
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional
import subprocess
import logging

class BaseGenerator(ABC):
    """Abstract base class for all emulator generators"""
    
    def __init__(self, system: str, rom: Path, core: Optional[str], platform):
        self.system = system
        self.rom = rom
        self.core = core
        self.platform = platform
        self.process: Optional[subprocess.Popen] = None
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def build_command(self) -> List[str]:
        """Build command-line arguments for emulator"""
        pass
    
    def configure(self):
        """Configure emulator (override in subclasses)"""
        pass
    
    def launch(self) -> int:
        """Launch the emulator and wait for exit"""
        try:
            self.logger.info(f"Launching {self.system} with {self.rom}")
            
            # Configure
            self.configure()
            
            # Build command
            command = self.build_command()
            self.logger.debug(f"Command: {' '.join(command)}")
            
            # Launch process
            self.process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            
            # Wait for completion
            exit_code = self.process.wait()
            self.logger.info(f"Emulator exited with code {exit_code}")
            
            return exit_code
            
        except Exception as e:
            self.logger.error(f"Failed to launch: {e}")
            return 1
    
    def terminate(self):
        """Terminate the emulator process"""
        if self.process and self.process.poll() is None:
            self.logger.warning("Terminating emulator process")
            self.process.terminate()
            self.process.wait(timeout=5)
```

### Acceptance Criteria
- [ ] BaseGenerator is abstract (cannot instantiate directly)
- [ ] Subclasses must implement `build_command()`
- [ ] `launch()` method handles errors gracefully
- [ ] Logging works correctly
- [ ] Process cleanup on termination

### Testing
```python
# Create test generator
class TestGenerator(BaseGenerator):
    def build_command(self):
        return ['/bin/echo', 'test']

# Test launch
gen = TestGenerator('test', Path('test.rom'), None, platform)
exit_code = gen.launch()
assert exit_code == 0
```

### Estimated Effort
2 days

---

## Issue #5: Implement RetroArch Generator

**Title:** `feat(emulators): implement RetroArch (libretro) generator`

**Labels:** `enhancement`, `phase-1`, `retroarch`, `P0`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P0 - Critical

### Description
Implement the RetroArch generator, porting functionality from `LibRetro.Generator.cs`. This is the highest priority emulator as it supports 80+ cores.

### Reference
C# Source: `/Users/bayramog/DevDirectory/GitRepos/emulatorlauncher/emulatorLauncher/Generators/LibRetro.Generator.cs`

### Tasks
- [ ] Create `emulators/retroarch.py`
- [ ] Implement RetroArch path detection
- [ ] Implement core path resolution
- [ ] Add config directory setup
- [ ] Implement command-line building
- [ ] Add fullscreen flag support
- [ ] Add verbose logging support
- [ ] Handle missing core errors

### Code Structure
```python
# emulators/retroarch.py
from pathlib import Path
from typing import List
from .base import BaseGenerator

class RetroArchGenerator(BaseGenerator):
    """RetroArch (libretro) emulator generator"""
    
    def build_command(self) -> List[str]:
        # Locate RetroArch
        retroarch_path = self.platform.get_emulator_path('retroarch')
        
        # Get core path
        core_path = self._get_core_path()
        
        # Build command
        command = [
            str(retroarch_path),
            '-L', str(core_path),
            str(self.rom),
            '--verbose',
        ]
        
        return command
    
    def _get_core_path(self) -> Path:
        """Locate RetroArch core library"""
        if not self.core:
            raise ValueError("Core name required for RetroArch")
        
        # Common core locations on macOS
        core_dirs = [
            Path.home() / 'Library/Application Support/RetroArch/cores',
            Path('/Applications/RetroArch.app/Contents/Resources/cores'),
            Path('/usr/local/lib/libretro'),
        ]
        
        for core_dir in core_dirs:
            core_path = core_dir / f'{self.core}_libretro.dylib'
            if core_path.exists():
                return core_path
        
        raise FileNotFoundError(f"Core {self.core} not found")
```

### RetroArch Core Naming
- Windows: `mesen_libretro.dll`
- macOS: `mesen_libretro.dylib`

### Core Locations (macOS)
```
~/Library/Application Support/RetroArch/cores/
/Applications/RetroArch.app/Contents/Resources/cores/
/usr/local/lib/libretro/
```

### Acceptance Criteria
- [ ] Can locate RetroArch executable
- [ ] Can find core libraries (.dylib files)
- [ ] Command-line built correctly
- [ ] Handles missing RetroArch gracefully
- [ ] Handles missing core gracefully
- [ ] Launches RetroArch successfully

### Manual Testing
```bash
# Test with actual RetroArch
python -m launcher \
  -system nes \
  -emulator retroarch \
  -core mesen \
  -rom ~/RetroBat/roms/nes/test.nes \
  --debug
```

### Estimated Effort
3-4 days

---

## Issue #6: Implement Configuration Loader

**Title:** `feat(config): implement configuration loader for es_systems.cfg`

**Labels:** `enhancement`, `phase-1`, `config`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P1 - High

### Description
Implement configuration loader to read `es_systems.cfg` and system configuration files from the RetroBat repository.

### Tasks
- [ ] Create `config/loader.py`
- [ ] Implement XML parser for `es_systems.cfg`
- [ ] Add system configuration lookup
- [ ] Add emulator configuration lookup
- [ ] Handle relative paths
- [ ] Add configuration caching

### Code Structure
```python
# config/loader.py
from pathlib import Path
from lxml import etree
from typing import Dict, Optional

class ConfigLoader:
    """Load RetroBat configuration files"""
    
    def __init__(self, base_path: Optional[Path] = None):
        if base_path is None:
            # Assume launcher is in RetroBat root
            base_path = Path(__file__).parent.parent.parent
        
        self.base_path = base_path
        self.system_path = base_path / 'system'
        self.es_systems_file = self.system_path / 'templates/emulationstation/es_systems.cfg'
    
    def load_system(self, system_name: str) -> Dict:
        """Load system configuration from es_systems.cfg"""
        tree = etree.parse(str(self.es_systems_file))
        
        # Find system
        system = tree.xpath(f"//system[name='{system_name}']")
        if not system:
            raise ValueError(f"System {system_name} not found")
        
        return self._parse_system(system[0])
    
    def _parse_system(self, element) -> Dict:
        """Parse system XML element"""
        return {
            'name': element.find('name').text,
            'fullname': element.find('fullname').text,
            'path': element.find('path').text,
            'extension': element.find('extension').text,
            'emulators': self._parse_emulators(element),
        }
    
    def _parse_emulators(self, system_element) -> Dict:
        """Parse emulator options for system"""
        emulators = {}
        for emulator in system_element.xpath('emulators/emulator'):
            name = emulator.get('name')
            cores = [c.text for c in emulator.xpath('cores/core')]
            emulators[name] = {'cores': cores}
        return emulators
```

### Acceptance Criteria
- [ ] Can parse `es_systems.cfg`
- [ ] Can lookup system by name
- [ ] Returns emulator options
- [ ] Handles missing systems gracefully
- [ ] Caches parsed configurations

### Testing
```python
loader = ConfigLoader()
nes_config = loader.load_system('nes')
assert nes_config['name'] == 'nes'
assert 'retroarch' in nes_config['emulators']
```

### Estimated Effort
2-3 days

---

## Issue #7: Implement Emulator Factory

**Title:** `feat(emulators): implement emulator factory pattern`

**Labels:** `enhancement`, `phase-1`, `core`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P1 - High

### Description
Implement the factory pattern to create emulator generator instances, mirroring the C# dictionary pattern in `Program.cs`.

### Tasks
- [ ] Create `emulators/factory.py`
- [ ] Implement generator registry
- [ ] Add factory method `create()`
- [ ] Handle unknown emulators
- [ ] Add logging

### Code Structure
```python
# emulators/factory.py
from typing import Dict, Type
from .base import BaseGenerator
from .retroarch import RetroArchGenerator

class EmulatorFactory:
    """Factory for creating emulator generator instances"""
    
    # Generator registry (like C# dictionary)
    _generators: Dict[str, Type[BaseGenerator]] = {
        'retroarch': RetroArchGenerator,
        'libretro': RetroArchGenerator,  # Alias
    }
    
    @classmethod
    def create(cls, emulator: str, system: str, rom, core, platform) -> BaseGenerator:
        """Create emulator generator instance"""
        generator_class = cls._generators.get(emulator.lower())
        
        if not generator_class:
            raise ValueError(f"Unknown emulator: {emulator}")
        
        return generator_class(
            system=system,
            rom=rom,
            core=core,
            platform=platform
        )
    
    @classmethod
    def register(cls, name: str, generator_class: Type[BaseGenerator]):
        """Register a new generator"""
        cls._generators[name.lower()] = generator_class
    
    @classmethod
    def list_emulators(cls) -> list:
        """List all registered emulators"""
        return list(cls._generators.keys())
```

### Acceptance Criteria
- [ ] Can create RetroArch generator
- [ ] Handles unknown emulators with clear error
- [ ] Supports emulator aliases (retroarch/libretro)
- [ ] Can list available emulators

### Testing
```python
factory = EmulatorFactory()
gen = factory.create('retroarch', 'nes', Path('test.nes'), 'mesen', platform)
assert isinstance(gen, RetroArchGenerator)
```

### Estimated Effort
1 day

---

## Issue #8: Implement Main Entry Point

**Title:** `feat(launcher): implement main entry point and integration`

**Labels:** `enhancement`, `phase-1`, `core`, `integration`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P0 - Critical

### Description
Implement the main entry point that integrates all components: CLI parser, platform detection, config loading, factory, and generator execution.

### Tasks
- [ ] Create `launcher/__main__.py`
- [ ] Integrate CLI parser
- [ ] Add platform detection
- [ ] Add config loading
- [ ] Integrate factory and generator
- [ ] Add logging configuration
- [ ] Add error handling
- [ ] Add exit code handling

### Code Structure
```python
# launcher/__main__.py
import sys
import logging
from pathlib import Path

from .cli.parser import ArgumentParser
from .platform.macos import MacOSPlatform
from .config.loader import ConfigLoader
from .emulators.factory import EmulatorFactory
from .utils.logger import setup_logging

def main():
    """Main entry point for emulator launcher"""
    try:
        # Parse arguments
        parser = ArgumentParser()
        args = parser.parse()
        
        # Setup logging
        setup_logging(debug=args.debug)
        logger = logging.getLogger('launcher')
        
        logger.info(f"Launching {args.system} - {args.emulator} - {args.rom}")
        
        # Initialize platform
        platform = MacOSPlatform()
        
        # Load configuration (optional for MVP)
        # config = ConfigLoader()
        # system_config = config.load_system(args.system)
        
        # Create generator
        factory = EmulatorFactory()
        generator = factory.create(
            emulator=args.emulator,
            system=args.system,
            rom=Path(args.rom),
            core=args.core,
            platform=platform
        )
        
        # Launch emulator
        exit_code = generator.launch()
        
        logger.info(f"Launcher exiting with code {exit_code}")
        sys.exit(exit_code)
        
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
```

### Logging Setup
```python
# utils/logger.py
import logging
from pathlib import Path

def setup_logging(debug: bool = False):
    """Configure logging"""
    level = logging.DEBUG if debug else logging.INFO
    
    log_dir = Path.home() / 'Library/Logs/RetroBat'
    log_dir.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        level=level,
        format='[%(asctime)s] %(levelname)s [%(name)s]: %(message)s',
        handlers=[
            logging.FileHandler(log_dir / 'launcher.log'),
            logging.StreamHandler()
        ]
    )
```

### Acceptance Criteria
- [ ] Can run: `python -m launcher --help`
- [ ] All components integrated correctly
- [ ] Errors logged and handled gracefully
- [ ] Exit codes match expectations (0 = success)
- [ ] Logs written to ~/Library/Logs/RetroBat/launcher.log

### Manual Testing
```bash
# Full integration test
python -m launcher \
  -system nes \
  -emulator retroarch \
  -core mesen \
  -rom ~/RetroBat/roms/nes/SuperMarioBros.nes \
  --debug
```

### Estimated Effort
1-2 days

---

## Issue #9: Create Unit Tests

**Title:** `test(launcher): create unit tests for core components`

**Labels:** `testing`, `phase-1`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P1 - High

### Description
Create comprehensive unit tests for all core components to ensure reliability and facilitate future refactoring.

### Tasks
- [ ] Set up pytest configuration
- [ ] Create `tests/` directory structure
- [ ] Write tests for CLI parser
- [ ] Write tests for platform layer
- [ ] Write tests for base generator
- [ ] Write tests for RetroArch generator
- [ ] Write tests for factory
- [ ] Add test fixtures and mocks
- [ ] Set up test coverage reporting

### Test Structure
```
tests/
├── __init__.py
├── conftest.py              # Fixtures
├── test_cli_parser.py
├── test_platform_macos.py
├── test_base_generator.py
├── test_retroarch.py
├── test_factory.py
└── test_integration.py
```

### Example Tests
```python
# tests/test_platform_macos.py
import pytest
from launcher.platform.macos import MacOSPlatform

def test_get_emulator_path_retroarch(tmp_path):
    # Mock RetroArch installation
    retroarch = tmp_path / 'RetroArch.app/Contents/MacOS/RetroArch'
    retroarch.parent.mkdir(parents=True)
    retroarch.touch()
    
    platform = MacOSPlatform()
    # Test would need to mock Path.exists()
    
def test_normalize_path_windows_to_macos():
    platform = MacOSPlatform()
    result = platform.normalize_path('C:\\RetroBat\\roms\\nes\\game.nes')
    assert '\\' not in str(result)
    assert not str(result).startswith('C:')
```

### Acceptance Criteria
- [ ] All tests pass: `pytest tests/`
- [ ] Test coverage > 80%
- [ ] Tests run in CI/CD
- [ ] Mock external dependencies (file system, processes)

### Estimated Effort
2-3 days

---

## Issue #10: Create End-to-End POC Test

**Title:** `test(launcher): create end-to-end proof-of-concept test`

**Labels:** `testing`, `phase-1`, `integration`, `P0`  
**Milestone:** Phase 1 - MVP  
**Assignee:** @bayramog  
**Priority:** P0 - Critical

### Description
Create an end-to-end test that launches an actual game with RetroArch on macOS, proving the MVP is functional.

### Prerequisites
- [ ] RetroArch installed (Homebrew or official)
- [ ] At least one core installed (e.g., mesen for NES)
- [ ] Test ROM file available (legally obtained)

### Tasks
- [ ] Install RetroArch: `brew install --cask retroarch`
- [ ] Install test core via RetroArch UI
- [ ] Create test ROM or use homebrew ROM
- [ ] Create integration test script
- [ ] Document test setup process
- [ ] Add troubleshooting guide

### Test Script
```bash
#!/bin/bash
# tests/integration/test_e2e.sh

echo "🎮 RetroBat macOS Launcher - E2E Test"
echo ""

# Check RetroArch
if ! command -v retroarch &> /dev/null; then
    echo "❌ RetroArch not found. Install with: brew install --cask retroarch"
    exit 1
fi
echo "✅ RetroArch found"

# Check core
CORE_PATH="$HOME/Library/Application Support/RetroArch/cores/mesen_libretro.dylib"
if [ ! -f "$CORE_PATH" ]; then
    echo "❌ Mesen core not found. Install via RetroArch UI."
    exit 1
fi
echo "✅ Mesen core found"

# Check test ROM
TEST_ROM="tests/fixtures/test.nes"
if [ ! -f "$TEST_ROM" ]; then
    echo "❌ Test ROM not found"
    exit 1
fi
echo "✅ Test ROM found"

# Launch test
echo ""
echo "�� Launching test..."
python -m launcher \
  -system nes \
  -emulator retroarch \
  -core mesen \
  -rom "$TEST_ROM" \
  --debug

EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Launch successful!"
else
    echo "❌ Launch failed with exit code $EXIT_CODE"
fi

exit $EXIT_CODE
```

### Success Criteria
- [ ] Script runs without errors
- [ ] RetroArch launches
- [ ] Game displays on screen
- [ ] Can control game with keyboard/controller
- [ ] Clean exit when quitting
- [ ] Logs written correctly

### Documentation
Create `docs/testing/E2E_SETUP.md` with:
- RetroArch installation steps
- Core installation guide
- Test ROM setup
- Troubleshooting common issues

### Estimated Effort
1-2 days (including setup)

---

## Summary

### Total Issues: 10
### Total Estimated Effort: 18-27 days (3-4 weeks)

### Dependencies
```
Issue #1 → Issue #2, #3, #4
Issue #2, #3, #4 → Issue #5, #6, #7
Issue #5, #6, #7 → Issue #8
Issue #8 → Issue #9, #10
```

### Critical Path
```
#1 (Structure) → #2 (CLI) → #3 (Platform) → #4 (Base) → 
#5 (RetroArch) → #7 (Factory) → #8 (Main) → #10 (E2E Test)
```

### Milestone: Phase 1 - MVP Complete
**Exit Criteria:**
- ✅ Can launch NES game via RetroArch on macOS
- ✅ Logs written and readable
- ✅ Error handling works
- ✅ Unit tests passing (>80% coverage)
- ✅ E2E test successful

---

## How to Create These Issues on GitHub

1. Go to: https://github.com/bayramog/retrobat/issues
2. Click "New Issue"
3. Copy/paste each issue above
4. Set appropriate labels and milestone
5. Assign to yourself

Or use GitHub CLI (if available):
```bash
gh issue create --title "TITLE" --body "BODY" --label "enhancement,phase-1"
```

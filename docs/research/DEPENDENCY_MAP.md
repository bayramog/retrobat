# RetroBat Dependency Map

**Date:** 2026-02-20  
**Purpose:** Map all dependencies for Windows and identify macOS equivalents

---

## 1. Runtime Dependencies

### 1.1 Core Binaries

| Component | Platform | Purpose | Location | macOS Equivalent |
|-----------|----------|---------|----------|------------------|
| emulatorLauncher.exe | Windows | Emulator launcher | Downloaded | **Python launcher (NEW)** |
| EmulationStation | Windows | Frontend | Downloaded | EmulationStation (Homebrew) |
| RetroArch | Windows | Multi-emulator | Downloaded | RetroArch (Homebrew/Official) |

### 1.2 Build Tools

| Tool | Purpose | Windows Path | macOS Equivalent |
|------|---------|--------------|------------------|
| wget.exe | Downloads | system/tools/wget.exe | `curl` (native) |
| curl.exe | HTTP client | system/tools/curl.exe | `curl` (native) |
| 7za.exe | Archive extraction | system/tools/7za.exe | `tar`/`unzip` (native) |
| RetroBuild.exe | Build manager | ./ | **Python script (NEW)** |

### 1.3 .NET Components

| Component | Type | Purpose | macOS Strategy |
|-----------|------|---------|----------------|
| RetroBuild.exe | .NET Console | Build system | Rewrite in Python |
| InstallerHost.exe | .NET GUI | Installer | Not needed (dmg/pkg) |
| emulatorLauncher.exe | .NET Console | Core launcher | Rewrite in Python |

---

## 2. Emulator Dependencies

### 2.1 Tier 1: Cross-Platform (High Priority)

| Emulator | Windows | macOS | Installation Method | Priority |
|----------|---------|-------|---------------------|----------|
| RetroArch | ✅ | ✅ | Homebrew / Official | **P0** |
| PPSSPP | ✅ | ✅ | Homebrew / Official | **P0** |
| Dolphin | ✅ | ✅ | Homebrew / Official | **P0** |
| DeSmuME | ✅ | ✅ | Homebrew | **P1** |
| mGBA | ✅ | ✅ | Homebrew | **P1** |
| Citra/Lime3DS | ✅ | ✅ | Community builds | **P1** |
| melonDS | ✅ | ✅ | Homebrew | **P1** |
| Duckstation | ✅ | ✅ | Official builds | **P1** |
| PCSX2 | ✅ | ✅ | Official builds | **P2** |

### 2.2 Tier 2: Windows-Only (Defer/Skip)

| Emulator | Systems | Why Skip |
|----------|---------|----------|
| Cemu | Wii U | Windows/Linux only |
| Xenia | Xbox 360 | Windows only |
| RPCS3 | PS3 | Limited macOS support |
| Project64 | N64 | Windows only (use RetroArch) |
| Most arcade emulators | Arcade | Windows-specific (use RetroArch/MAME) |

---

## 3. Python Dependencies (Proposed)

### 3.1 Core Libraries

```python
# requirements.txt
PyYAML>=6.0          # Config file parsing
lxml>=4.9.0          # XML handling (es_systems.cfg)
psutil>=5.9.0        # Process management
requests>=2.31.0     # HTTP downloads
pathlib              # Path handling (stdlib)
argparse             # CLI parsing (stdlib)
subprocess           # Process execution (stdlib)
logging              # Logging (stdlib)
```

### 3.2 Optional Libraries

```python
# requirements-dev.txt
pytest>=7.4.0        # Testing
black>=23.0.0        # Code formatting
pylint>=2.17.0       # Linting
mypy>=1.4.0          # Type checking
```

---

## 4. System Dependencies (macOS)

### 4.1 Required

| Tool | Purpose | Installation |
|------|---------|--------------|
| Python 3.11+ | Launcher runtime | `brew install python@3.11` |
| curl | Downloads | Native (macOS built-in) |
| tar | Archive extraction | Native (macOS built-in) |
| unzip | Archive extraction | Native (macOS built-in) |

### 4.2 Optional

| Tool | Purpose | Installation |
|------|---------|--------------|
| Homebrew | Package manager | `/bin/bash -c "$(curl...)"` |
| git | Version control | Native or `xcode-select --install` |

---

## 5. EmulationStation Dependencies

### 5.1 Installation Options

**Option 1: Homebrew** (Recommended)
```bash
brew install emulationstation
```

**Option 2: Official Builds**
- Download from EmulationStation releases
- macOS `.app` bundle

**Option 3: Build from Source**
- Clone RetroBat-Official/emulationstation
- Build for macOS

### 5.2 Configuration Files
- `es_systems.cfg` - System definitions
- `es_settings.cfg` - Frontend settings
- `es_input.cfg` - Controller mappings

**Path Changes Needed:**
- Windows: `%HOME%\emulatorLauncher.exe`
- macOS: `$HOME/emulatorLauncher.py` or `/usr/local/bin/emulatorLauncher`

---

## 6. Path Mapping

### 6.1 Directory Structure

| Purpose | Windows | macOS Proposal |
|---------|---------|----------------|
| RetroBat root | `C:\RetroBat` | `/Applications/RetroBat.app` or `~/RetroBat` |
| ROMs | `C:\RetroBatoms` | `~/RetroBat/roms` |
| Emulators | `C:\RetroBat\emulators` | `/Applications` or `~/RetroBat/emulators` |
| BIOS | `C:\RetroBatios` | `~/RetroBat/bios` |
| Saves | `C:\RetroBat\saves` | `~/Library/Application Support/RetroBat/saves` |
| Screenshots | `C:\RetroBat\screenshots` | `~/Pictures/RetroBat` |
| Configs | `C:\RetroBat\emulationstation` | `~/Library/Application Support/RetroBat/config` |

### 6.2 Environment Variables

| Windows | macOS | Purpose |
|---------|-------|---------|
| `%HOME%` | `$HOME` | RetroBat root |
| `%APPDATA%` | `~/Library/Application Support` | App data |
| `%USERPROFILE%` | `$HOME` | User directory |
| `%TEMP%` | `$TMPDIR` | Temporary files |

---

## 7. RetroArch Core Dependencies

### 7.1 High-Priority Cores (macOS Compatible)

| Core | Systems | Status |
|------|---------|--------|
| mesen | NES | ✅ |
| snes9x | SNES | ✅ |
| genesis_plus_gx | Genesis/MD | ✅ |
| gambatte | Game Boy/GBC | ✅ |
| mgba | GBA | ✅ |
| beetle_psx_hw | PS1 | ✅ |
| mupen64plus_next | N64 | ✅ |
| mame2003_plus | Arcade | ✅ |
| fbneo | Arcade | ✅ |

### 7.2 Installation
```bash
# RetroArch auto-downloads cores
# Or manually from: http://buildbot.libretro.com/nightly/apple/osx/
```

---

## 8. Build Process Dependencies

### 8.1 Windows Build Process

```
1. RetroBuild.exe
2. Reads build.ini
3. Downloads components (wget/curl)
4. Extracts archives (7za)
5. Copies files
6. Creates installer
```

### 8.2 Proposed macOS Build Process

```
1. build.py (Python script)
2. Reads build.yaml
3. Downloads components (curl)
4. Extracts archives (tar/unzip)
5. Copies files
6. Creates .app bundle or .dmg
```

### 8.3 Build Script Dependencies

```python
# build/requirements.txt
requests>=2.31.0      # Downloads
PyYAML>=6.0           # Config parsing
py2app>=0.28.0        # .app bundle creation (optional)
dmgbuild>=1.6.0       # .dmg creation (optional)
```

---

## 9. Download URL Mapping

### 9.1 Emulator Sources

| Component | Windows URL | macOS URL |
|-----------|-------------|-----------|
| EmulationStation | GitHub releases | Homebrew or GitHub |
| RetroArch | buildbot.libretro.com/windows | buildbot.libretro.com/apple/osx |
| PPSSPP | ppsspp.org/downloads | ppsspp.org/downloads |
| Dolphin | dolphin-emu.org | dolphin-emu.org |

### 9.2 Component URLs (build.ini equivalent)

```yaml
# build.yaml (proposed)
components:
  emulationstation:
    url_macos: "https://github.com/RetroBat-Official/emulationstation/releases/download/continuous-master/EmulationStation-macOS.zip"
  
  retroarch:
    url_macos: "https://buildbot.libretro.com/stable/1.16.0/apple/osx/universal/RetroArch.dmg"
  
  launcher:
    # Our own Python launcher
    builtin: true
```

---

## 10. Development Dependencies

### 10.1 Development Environment

| Tool | Purpose | Installation |
|------|---------|--------------|
| Python 3.11+ | Development | `brew install python@3.11` |
| VS Code | IDE | Download or `brew install --cask visual-studio-code` |
| Git | Version control | Native or `xcode-select --install` |
| pytest | Testing | `pip install pytest` |

### 10.2 Testing Requirements

```python
# requirements-test.txt
pytest>=7.4.0
pytest-cov>=4.1.0        # Coverage
pytest-mock>=3.11.0      # Mocking
pytest-timeout>=2.1.0    # Timeout handling
```

---

## 11. Distribution Dependencies

### 11.1 Package Formats

| Format | Purpose | Tool |
|--------|---------|------|
| .app bundle | macOS application | py2app or manual |
| .dmg | Installer image | dmgbuild or hdiutil |
| .pkg | System installer | pkgbuild |
| Homebrew cask | Package manager | brew cask |

### 11.2 Code Signing (Future)

```bash
# Requires Apple Developer Account
codesign --sign "Developer ID" RetroBat.app
```

---

## 12. Dependency Installation Script

### 12.1 Proposed Setup Script

```bash
#!/bin/bash
# setup-macos.sh

echo "🎮 Setting up RetroBat for macOS..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Install with: brew install python@3.11"
    exit 1
fi

# Check Homebrew
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Install from: https://brew.sh"
    exit 1
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Install emulators (optional)
echo "🎮 Install RetroArch? (y/n)"
read -r response
if [[ "$response" == "y" ]]; then
    brew install --cask retroarch
fi

echo "✅ Setup complete!"
```

---

## 13. Dependency Matrix

### 13.1 Complete Overview

| Dependency | Windows | macOS | Installation | Priority |
|------------|---------|-------|--------------|----------|
| Python 3.11+ | Optional | ✅ Required | Homebrew | P0 |
| emulatorLauncher.exe | ✅ | ❌ (Rewrite) | Built-in | P0 |
| EmulationStation | ✅ | ✅ | Homebrew | P0 |
| RetroArch | ✅ | ✅ | Homebrew | P0 |
| wget.exe | ✅ | ❌ (use curl) | Native | P0 |
| 7za.exe | ✅ | ❌ (use tar) | Native | P0 |
| RetroBuild.exe | ✅ | ❌ (Rewrite) | Python | P1 |
| PPSSPP | ✅ | ✅ | Homebrew | P1 |
| Dolphin | ✅ | ✅ | Homebrew | P1 |

---

## 14. Next Steps

1. ✅ Document dependencies (DONE)
2. ⬜ Create Python virtual environment
3. ⬜ Install development dependencies
4. ⬜ Create requirements.txt files
5. ⬜ Test emulator availability on macOS
6. ⬜ Create setup script

---

**Document Version:** 1.0  
**Date:** 2026-02-20  
**Status:** Complete

# RetroBat Codebase Architecture Analysis

**Date:** 2026-02-20  
**Branch:** research/initial-codebase-analysis  
**Purpose:** Deep analysis of RetroBat's Windows architecture to inform macOS port strategy

---

## Executive Summary

RetroBat is a Windows-focused retro gaming distribution system that:
- Configures and launches 125+ emulators across 230+ gaming systems
- Uses EmulationStation as frontend interface
- Employs a separate `emulatorLauncher.exe` for emulator execution
- Relies heavily on Windows-specific tooling (.NET executables, PowerShell, Windows paths)

**Key Finding:** The core emulator launching logic is encapsulated in an external Windows binary (`emulatorLauncher.exe`), which will require complete reimplementation for macOS.

---

## 1. Core Architecture

### 1.1 Main Components

```
RetroBat/
├── RetroBuild.exe          # Build/download manager (.NET/Mono)
├── InstallerHost.exe       # Installation GUI (.NET/Mono)
├── emulatorLauncher.exe    # CORE: Launches emulators (NOT in repo)
├── build.ini               # Build configuration
├── system/
│   ├── configgen/          # Emulator/system mappings
│   ├── templates/          # Config templates per emulator
│   │   └── emulationstation/
│   │       └── es_systems.cfg  # System definitions
│   ├── resources/          # Global configs
│   └── tools/              # Windows utilities (wget, curl, 7za)
└── roms/                   # Game storage (runtime)
```

### 1.2 Execution Flow

```
User selects game in EmulationStation
         ↓
EmulationStation parses es_systems.cfg
         ↓
Calls: emulatorLauncher.exe with arguments:
  -system <system>
  -emulator <emulator>
  -core <core>
  -rom <rom_path>
  -gameinfo <xml>
  %CONTROLLERSCONFIG%
         ↓
emulatorLauncher.exe:
  1. Reads system config
  2. Locates emulator binary
  3. Generates emulator-specific config
  4. Launches emulator process
  5. Monitors and manages process
  6. Cleans up on exit
         ↓
User plays game
```

**Critical Observation:** `emulatorLauncher.exe` is downloaded at build time, not present in source repository. This is the Windows-specific launcher that needs macOS equivalent.

---

## 2. Configuration System (configgen)

### 2.1 Purpose
The `configgen/` directory contains list files that map:
- Systems to emulators
- Emulators to their names/paths
- LibRetro cores to names
- Templates to files
- Directory tree structure

### 2.2 Key Insight
This is a **data-driven configuration system**, not hardcoded logic. We can reuse these mappings for macOS.

**Files:** emulators_names.lst (125 emulators), systems_names.lst (230+ systems), lrcores_names.lst, templates_files.lst, retrobat_tree.lst

---

## 3. EmulationStation Integration

### 3.1 es_systems.cfg
- 5,557 lines defining all supported systems
- Each system specifies: Name, ROM path, extensions, launch command, emulators/cores

### 3.2 Example System Definition
```xml
<system>
  <name>mame</name>
  <command>"%HOME%\emulatorLauncher.exe" -system %SYSTEM% -emulator %EMULATOR% -core %CORE% -rom %ROM%</command>
</system>
```

**Path Handling:** Uses Windows-style paths (`\`), `%HOME%` environment variable.

---

## 4. Build System

### 4.1 build.ini
- Defines versions, architectures, download URLs
- emulatorLauncher comes from: `https://github.com/RetroBat-Official/emulatorlauncher`

### 4.2 Windows-Specific Tools
- `wget.exe`, `curl.exe`, `7za.exe` - All Windows PE32 executables
- RetroBuild.exe - .NET/Mono console application
- InstallerHost.exe - .NET/Mono GUI application

---

## 5. Windows-Specific Dependencies

| Component | Type | macOS Equivalent Needed |
|-----------|------|------------------------|
| emulatorLauncher.exe | .NET binary | **YES - Complete rewrite** |
| RetroBuild.exe | .NET binary | Python script |
| wget.exe / curl.exe | Windows binary | curl (native macOS) |
| 7za.exe | Windows binary | tar/unzip (native) |

**Path Format:**
- Windows: `\`, `C:\`, `%HOME%`
- macOS: `/`, `/Users/`, `$HOME`

---

## 6. EmulatorLauncher Deep Dive

### 6.1 Responsibilities
1. Parse command-line arguments
2. Read system/emulator configuration
3. Generate runtime config files
4. Locate emulator executable
5. Build emulator command line
6. Launch emulator subprocess
7. Monitor process
8. Handle save states, screenshots
9. Clean up temporary files

### 6.2 Where It Comes From
**Upstream:** https://github.com/RetroBat-Official/emulatorlauncher  
**Downloaded during build** from `batocera-ports.zip`

---

## 7. Critical Findings for macOS Port

### 7.1 High-Impact Items

1. **emulatorLauncher.exe must be reimplemented**
   - Core functionality of RetroBat
   - Windows-specific binary
   - Estimated complexity: **HIGH**

2. **Path handling requires abstraction layer**
   - Affects: es_systems.cfg, templates, all configs

3. **Build system needs macOS support**
   - RetroBuild.exe needs Python equivalent
   - Download URLs may differ for macOS emulators

4. **Emulator binary availability**
   - Not all 125 Windows emulators have macOS builds
   - RetroArch is highest priority (cross-platform)

### 7.2 Low-Impact Items (Portable)

1. Configuration data (`.lst` files)
2. EmulationStation (cross-platform)
3. ROM management (platform-agnostic)

---

## 8. macOS Emulator Availability

### 8.1 High-Priority Targets (Available on macOS)

| Emulator | Systems | macOS Status |
|----------|---------|--------------|
| **RetroArch** | Multi (80+ cores) | ✅ Native |
| PPSSPP | PSP | ✅ Native |
| Dolphin | GameCube/Wii | ✅ Native |
| DeSmuME | NDS | ✅ Native |
| mGBA | GBA | ✅ Native |
| Citra | 3DS | ✅ Native (forks) |
| PCSX2 | PS2 | ✅ Native |
| Duckstation | PS1 | ✅ Native |

### 8.2 Windows-Only (Skip Phase 1)
- Cemu (Wii U)
- Xenia (Xbox 360)
- RPCS3 (PS3) - Limited support

---

## 9. Recommended Phase 1 Scope

### 9.1 Systems to Support First
1. **RetroArch-based:** NES, SNES, Genesis, GB, GBA, PS1, N64, Arcade
2. **Standalone:** PPSSPP (PSP), Dolphin (GameCube)

### 9.2 Out of Scope for Phase 1
- Windows-only emulators
- Xbox/Xbox 360 systems
- Advanced features (WiimoteGun, BatGui)

---

## 10. Architecture Recommendations

### 10.1 Proposed macOS Structure

```
retrobat-macos/
├── launcher/
│   ├── main.py              # Entry point (replaces emulatorLauncher.exe)
│   ├── platform/
│   │   ├── detect.py        # OS detection
│   │   ├── paths.py         # Path abstraction
│   │   └── process.py       # Process management
│   ├── config/
│   │   ├── loader.py        # Config parsing
│   │   ├── generator.py     # Config generation
│   │   └── templates.py     # Template handling
│   ├── emulators/
│   │   ├── base.py          # Base emulator class
│   │   ├── retroarch.py     # RetroArch launcher
│   │   ├── ppsspp.py        # PPSSPP launcher
│   │   └── ...
│   └── utils/
│       ├── logger.py
│       └── validation.py
├── build/
│   ├── build.py             # Python build script
│   └── download.py          # Download manager
└── system/                  # Existing (portable)
```

### 10.2 Technology Stack
- **Language:** Python 3.11+
- **Dependencies:**
  - `PyYAML` - Config parsing
  - `lxml` - XML handling
  - `psutil` - Process management
  - `requests` - Downloads
- **Build Tools:**
  - Native `curl`, `tar`, `unzip`
  - `Homebrew` for emulator distribution

---

## 11. Risk Assessment

### 11.1 High Risk
1. emulatorLauncher reimplementation (unknown internals)
2. Path handling everywhere (hardcoded in many files)
3. Emulator binary availability

### 11.2 Medium Risk
1. Configuration compatibility
2. EmulationStation integration differences

### 11.3 Low Risk
1. ROM management
2. Configuration data
3. Themes/decorations

---

## 12. Next Steps

### 12.1 Immediate Actions
1. ✅ Complete architecture analysis (DONE)
2. ⬜ Create dependency map document
3. ⬜ Design platform abstraction layer
4. ⬜ Create technical design for macOS launcher
5. ⬜ Set up development environment
6. ⬜ Create proof-of-concept: RetroArch launcher

### 12.2 Phase 0 Deliverables
- [x] Branching and governance model
- [x] PR/issue templates
- [x] Local push guardrails
- [x] Test gate workflow
- [ ] Architecture analysis (this document)
- [ ] Dependency mapping
- [ ] Technical design document

---

## 13. Appendix: Analysis Summary

### 13.1 Key Files Analyzed
- `build.ini` - Build configuration
- `system/configgen/*.lst` - System/emulator mappings (5 files)
- `system/templates/emulationstation/es_systems.cfg` - System definitions (5,557 lines)
- `system/resources/retrobat_template.ini` - Global configuration
- `system/templates/*` - 97 emulator template directories

### 13.2 Statistics
- Total systems defined: 230+
- Total emulators supported: 125
- Total es_systems.cfg lines: 5,557
- Total templates directories: 97

### 13.3 Binary Analysis
- RetroBuild.exe: PE32 .NET/Mono console
- InstallerHost.exe: PE32 .NET/Mono GUI
- emulatorLauncher.exe: External download (not in repo)

---

**Document Version:** 1.0  
**Author:** Research Phase Analysis  
**Date:** 2026-02-20  
**Status:** Complete

---

## UPDATE: Upstream Repository Analysis (2026-02-20)

### Forked Repositories
After initial analysis, we've now forked and analyzed the upstream source code:

**EmulationStation:** https://github.com/bayramog/emulationstation
- Fork of RetroBat-Official/emulationstation
- Frontend UI (C++)
- Can use existing macOS builds (Homebrew)

**EmulatorLauncher:** https://github.com/bayramog/emulatorlauncher  
- Fork of RetroBat-Official/emulatorlauncher
- **C# (.NET) - 50,000+ lines of code**
- 207 generator files (one per emulator)
- Generator pattern architecture

### Key Discovery: Generator Architecture

The EmulatorLauncher uses a **Generator Pattern**:
```csharp
// From Program.cs (1,163 lines)
static Dictionary<string, Func<Generator>> generators = {
    { "retroarch", () => new LibRetroGenerator() },
    { "ppsspp", () => new PpssppGenerator() },
    { "dolphin", () => new DolphinGenerator() },
    // ... 125+ emulators
}
```

**This confirms our Python architecture is the right approach!**

### Updated Effort Estimate

| Component | Lines | Effort |
|-----------|-------|--------|
| Core Launcher | ~400 Python | 1 week |
| LibRetro Generator | ~300 Python | 1 week |
| PPSSPP + Dolphin | ~450 Python | 1 week |
| **Total MVP** | **~1,150 Python** | **3 weeks** |

### Recommendation Update
✅ **Python generator pattern confirmed as best approach**  
✅ **Port incrementally: RetroArch → PPSSPP → Dolphin**  
✅ **~3-4 weeks for MVP** (revised from 6 weeks)

See detailed analysis: [UPSTREAM_ANALYSIS.md](UPSTREAM_ANALYSIS.md)

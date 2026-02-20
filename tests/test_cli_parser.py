"""
Unit tests for CLI argument parser.
"""

import pytest
from pathlib import Path
from launcher.cli.parser import ArgumentParser


class TestArgumentParser:
    """Test cases for ArgumentParser class."""

    def test_parser_creation(self):
        """Test that parser can be created."""
        parser = ArgumentParser()
        assert parser is not None
        assert parser.parser is not None

    def test_version_output(self):
        """Test that --version works."""
        parser = ArgumentParser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse(["--version"])
        assert exc_info.value.code == 0

    def test_required_arguments(self):
        """Test that required arguments are enforced."""
        parser = ArgumentParser()
        
        # Missing all required args
        with pytest.raises(SystemExit):
            parser.parse([])

    def test_valid_arguments(self, tmp_path):
        """Test parsing valid arguments."""
        # Create a temporary ROM file
        rom_file = tmp_path / "test.nes"
        rom_file.write_text("test rom")
        
        parser = ArgumentParser()
        args = parser.parse([
            "-system", "nes",
            "-emulator", "retroarch",
            "-core", "mesen",
            "-rom", str(rom_file),
        ])
        
        assert args.system == "nes"
        assert args.emulator == "retroarch"
        assert args.core == "mesen"
        assert args.rom == rom_file

    def test_debug_flags(self, tmp_path):
        """Test debug and dry-run flags."""
        rom_file = tmp_path / "test.nes"
        rom_file.write_text("test")
        
        parser = ArgumentParser()
        args = parser.parse([
            "-system", "nes",
            "-emulator", "retroarch",
            "-rom", str(rom_file),
            "--debug",
            "--dry-run",
        ])
        
        assert args.debug is True
        assert args.dry_run is True

    def test_rom_file_not_found(self):
        """Test that non-existent ROM file raises error."""
        parser = ArgumentParser()
        with pytest.raises(SystemExit):
            parser.parse([
                "-system", "nes",
                "-emulator", "retroarch",
                "-rom", "/nonexistent/file.nes",
            ])

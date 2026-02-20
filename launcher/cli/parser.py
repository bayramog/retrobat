"""
Command-line argument parser for RetroBat Launcher.

Parses arguments from EmulationStation in the format:
    python -m launcher -system <system> -emulator <emulator> -core <core> -rom <rom>
"""

import argparse
import sys
from pathlib import Path
from typing import Optional


class ArgumentParser:
    """Parse command-line arguments from EmulationStation."""

    def __init__(self):
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """Create and configure the argument parser."""
        parser = argparse.ArgumentParser(
            prog="retrobat-launcher",
            description="RetroBat Emulator Launcher - macOS Edition",
            epilog="For more information, visit: https://github.com/bayramog/retrobat",
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )

        # Version
        parser.add_argument(
            "--version",
            action="version",
            version="RetroBat Launcher v1.0.0-alpha (macOS)",
        )

        # Required arguments
        required = parser.add_argument_group("required arguments")
        required.add_argument(
            "-system",
            required=True,
            help="System name (e.g., nes, snes, ps1)",
        )
        required.add_argument(
            "-emulator",
            required=True,
            help="Emulator name (e.g., retroarch, ppsspp)",
        )
        required.add_argument(
            "-rom",
            required=True,
            type=Path,
            help="Path to ROM file",
        )

        # Optional arguments
        optional = parser.add_argument_group("optional arguments")
        optional.add_argument(
            "-core",
            help="Emulator core (for libretro/retroarch)",
        )
        optional.add_argument(
            "-gameinfo",
            type=Path,
            help="Path to game metadata XML file",
        )
        optional.add_argument(
            "--controllers-config",
            type=Path,
            help="Path to controllers configuration file",
        )

        # Debug options
        debug = parser.add_argument_group("debug options")
        debug.add_argument(
            "--debug",
            action="store_true",
            help="Enable debug output",
        )
        debug.add_argument(
            "--verbose",
            "-v",
            action="store_true",
            help="Enable verbose output",
        )
        debug.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would be executed without actually launching",
        )

        return parser

    def parse(self, args: Optional[list] = None) -> argparse.Namespace:
        """
        Parse command-line arguments.

        Args:
            args: List of arguments to parse. If None, uses sys.argv[1:]

        Returns:
            Parsed arguments namespace

        Raises:
            SystemExit: If arguments are invalid or --help/--version is used
        """
        parsed_args = self.parser.parse_args(args)

        # Validate ROM file exists
        if not parsed_args.rom.exists():
            self.parser.error(f"ROM file not found: {parsed_args.rom}")

        # Validate gameinfo file if provided
        if parsed_args.gameinfo and not parsed_args.gameinfo.exists():
            self.parser.error(f"Game info file not found: {parsed_args.gameinfo}")

        # Validate controllers config if provided
        if (
            parsed_args.controllers_config
            and not parsed_args.controllers_config.exists()
        ):
            self.parser.error(
                f"Controllers config file not found: {parsed_args.controllers_config}"
            )

        return parsed_args

    def print_help(self):
        """Print help message."""
        self.parser.print_help()


def main():
    """Test the argument parser."""
    parser = ArgumentParser()
    try:
        args = parser.parse()
        print("✅ Arguments parsed successfully!")
        print(f"   System: {args.system}")
        print(f"   Emulator: {args.emulator}")
        print(f"   Core: {args.core or 'N/A'}")
        print(f"   ROM: {args.rom}")
        print(f"   Debug: {args.debug}")
        return 0
    except SystemExit as e:
        return e.code


if __name__ == "__main__":
    sys.exit(main())

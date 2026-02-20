"""
Main entry point for the launcher.

This allows running the launcher as a module:
    python -m launcher [args]
"""

import sys
from .cli.parser import ArgumentParser


def main():
    """Main entry point."""
    # Parse command-line arguments
    parser = ArgumentParser()
    
    try:
        args = parser.parse()
        
        # Display parsed information (implementation placeholder)
        print("╔════════════════════════════════════════════════════════════╗")
        print("║        RetroBat Launcher - macOS Edition v1.0.0-alpha     ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print()
        print("📋 Configuration:")
        print(f"   System:      {args.system}")
        print(f"   Emulator:    {args.emulator}")
        print(f"   Core:        {args.core or 'N/A'}")
        print(f"   ROM:         {args.rom}")
        print()
        
        if args.debug or args.verbose:
            print("🐛 Debug Mode: ON")
            print(f"   Game Info:   {args.gameinfo or 'N/A'}")
            print(f"   Controllers: {args.controllers_config or 'N/A'}")
            print(f"   Dry Run:     {args.dry_run}")
            print()
        
        if args.dry_run:
            print("🔍 Dry Run Mode - Would execute:")
            print(f"   Launch {args.emulator} for {args.system}")
            print(f"   ROM: {args.rom.name}")
            print()
            print("✅ Dry run complete (no actual launch)")
            return 0
        
        print("⚠️  Launcher implementation coming soon!")
        print("    (Platform abstraction, generators, and process management)")
        print()
        print("✅ Arguments parsed successfully - ready for implementation")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
        return 130
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

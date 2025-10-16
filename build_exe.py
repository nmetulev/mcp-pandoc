#!/usr/bin/env python
"""Build script to create executable using PyInstaller."""
import subprocess
import sys
from pathlib import Path


def main():
    """Build the executable using PyInstaller."""
    print("Building mcp-pandoc executable with PyInstaller...")
    print("=" * 60)
    
    # Ensure we're in the project root
    project_root = Path(__file__).parent
    spec_file = project_root / "mcp-pandoc.spec"
    
    if not spec_file.exists():
        print(f"Error: Spec file not found at {spec_file}")
        sys.exit(1)
    
    # Run PyInstaller
    try:
        cmd = [
            sys.executable,
            "-m",
            "PyInstaller",
            "--clean",  # Clean cache before building
            str(spec_file)
        ]
        
        print(f"Running: {' '.join(cmd)}")
        print("-" * 60)
        
        result = subprocess.run(cmd, cwd=str(project_root), check=True)
        
        print("-" * 60)
        print("✓ Build completed successfully!")
        print(f"\nExecutable location: {project_root / 'dist' / 'mcp-pandoc.exe'}")
        print("\nYou can now use this executable for MSIX packaging.")
        
        return 0
        
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build failed with error code {e.returncode}")
        return e.returncode
    except FileNotFoundError:
        print("\n✗ Error: PyInstaller not found. Please install it first:")
        print("  pip install pyinstaller")
        return 1


if __name__ == "__main__":
    sys.exit(main())

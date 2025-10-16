#!/usr/bin/env python
"""Entry point script for PyInstaller packaging."""
import asyncio
import sys

# Add the package to the path if needed
from mcp_pandoc import server


def main():
    """Run the mcp-pandoc server."""
    asyncio.run(server.main())


if __name__ == "__main__":
    main()

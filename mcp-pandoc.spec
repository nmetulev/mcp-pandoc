# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec file for mcp-pandoc MCP server."""

block_cipher = None

a = Analysis(
    ['run_server.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        # Include example defaults files
        ('examples/defaults', 'examples/defaults'),
    ],
    hiddenimports=[
        'mcp',
        'mcp.server',
        'mcp.server.stdio',
        'mcp.types',
        'mcp.server.models',
        'pypandoc',
        'yaml',
        'pandocfilters',
        'panflute',
        'mcp_pandoc',
        'mcp_pandoc.server',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='mcp-pandoc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Keep console window for stdio communication
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

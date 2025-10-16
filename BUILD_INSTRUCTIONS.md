# Building mcp-pandoc as an Executable for MSIX Packaging

This guide explains how to build the mcp-pandoc MCP server as a standalone executable using PyInstaller, which can then be packaged into an MSIX for Windows distribution.

## Prerequisites

1. **Python 3.11 or higher** (as specified in pyproject.toml)
2. **Pandoc** - Must be installed on your system:
   - Download from: https://pandoc.org/installing.html
   - Or use: `winget install --id JohnMacFarlane.Pandoc`
3. **PyInstaller** - Will be installed in the steps below

## Step 1: Install PyInstaller

```powershell
pip install pyinstaller
```

## Step 2: Install Project Dependencies

Make sure all the project dependencies are installed:

```powershell
pip install -e .
```

Or install them directly:

```powershell
pip install mcp pyyaml pandoc pypandoc pandocfilters panflute
```

## Step 3: Build the Executable

### Option A: Using the build script (Recommended)

```powershell
python build_exe.py
```

### Option B: Using PyInstaller directly

```powershell
pyinstaller --clean mcp-pandoc.spec
```

## Step 4: Test the Executable

After building, the executable will be located at:
```
dist\mcp-pandoc.exe
```

You can test it by running:
```powershell
.\dist\mcp-pandoc.exe
```

Note: The executable expects stdio communication (it's an MCP server), so it will wait for input. Press Ctrl+C to exit.

## Step 5: Package into MSIX

Now you can use the `mcp-pandoc.exe` from the `dist` folder in your MSIX packaging process.

### Key considerations for MSIX:

1. **Include Pandoc**: Your MSIX package should either:
   - Bundle pandoc.exe with your application
   - Specify Pandoc as a dependency in your MSIX manifest
   - Document that users must install Pandoc separately

2. **File structure for MSIX**:
   ```
   YourMSIX/
   ├── mcp-pandoc.exe
   ├── examples/          (optional - included defaults)
   │   └── defaults/
   └── AppxManifest.xml   (your MSIX manifest)
   ```

3. **Example MSIX Manifest snippet**:
   ```xml
   <Application Id="MCPPandoc" Executable="mcp-pandoc.exe" EntryPoint="Windows.FullTrustApplication">
     <uap:VisualElements DisplayName="MCP Pandoc Server" ... />
   </Application>
   ```

## Troubleshooting

### Import Errors
If you get import errors when running the executable, add the missing modules to the `hiddenimports` list in `mcp-pandoc.spec`.

### Missing Files
If your application needs additional data files, add them to the `datas` list in `mcp-pandoc.spec`:
```python
datas=[
    ('path/to/source', 'path/in/bundle'),
],
```

### Large Executable Size
The executable includes Python and all dependencies. To reduce size:
- Use `upx=True` in the spec file (already enabled)
- Consider using `--onedir` instead of `--onefile` mode
- Exclude unnecessary modules in the `excludes` list

### Pandoc Not Found
The executable itself doesn't include Pandoc (a separate tool). Users must have:
- Pandoc installed on their system
- Pandoc in their PATH environment variable

## Build Artifacts

After building, you'll see these directories:
- `build/` - Temporary build files (can be deleted)
- `dist/` - Final executable location (this is what you need for MSIX)
- `__pycache__/` - Python cache (can be ignored)

## Next Steps for MSIX

1. Use the Windows Application Packaging Project in Visual Studio, or
2. Use the `MakeAppx.exe` command-line tool from the Windows SDK
3. Sign your MSIX package with a certificate

For more information on MSIX packaging:
- https://docs.microsoft.com/en-us/windows/msix/package/packaging-uwp-apps

## Additional Resources

- PyInstaller Documentation: https://pyinstaller.org/
- MCP Documentation: https://modelcontextprotocol.io/
- Pandoc Documentation: https://pandoc.org/

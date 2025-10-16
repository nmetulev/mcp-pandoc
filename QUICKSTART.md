# Quick Start: Building the Executable

## 1. Install PyInstaller
```powershell
pip install pyinstaller
```

## 2. Install Dependencies
```powershell
pip install -e .
```

## 3. Build the Executable
```powershell
python build_exe.py
```

## 4. Your executable is ready!
```
📁 Location: dist\mcp-pandoc.exe
```

## 5. Test it (optional)
```powershell
.\dist\mcp-pandoc.exe
# Press Ctrl+C to exit
```

---

**For detailed instructions, see:** `BUILD_INSTRUCTIONS.md`

**For MSIX packaging:** Use the `mcp-pandoc.exe` from the `dist` folder.

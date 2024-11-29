# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

# Including necessary files for PyInstaller
a = Analysis(
    ['main.py'],  # Main entry script
    pathex=['/path/to/your/project'],  # Path to your project directory (optional)
    binaries=[],
    # Include 'reactiontime.py' in the bundled application under the 'frontend/games' directory
    datas=[('frontend/games/ReactionTime.py', 'frontend/games')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# Compiling Python files into a PYZ archive
pyz = PYZ(a.pure)

# Creating the executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',  # Name of the executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Optional: enable UPX compression
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Run as a console application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# main.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    strip=False,
    upx=True,
    console=True,
    icon=None,
    onefile=True,   # This is the key part to bundle into one executable
    clean=True  # Ensures PyInstaller cleans up unnecessary files
)

# We don't need the COLLECT step in the case of onefile mode
# PyInstaller handles everything in a single file.

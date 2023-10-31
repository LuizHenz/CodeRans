# -- mode: python ; coding: utf-8 --

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('requirements.txt', '.'),
        ('install_deps.sh', '.'),
        ('pacote', './pacote'),
        # Aqui está a adição para o Pillow
        ('./venv/lib/python3.11/site-packages/PIL/**', 'PIL')
    ],
    hiddenimports=[
        'PIL._tkinter_finder'  # Adiciona a dependência escondida do Pillow
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='rans',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
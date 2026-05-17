# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
block_cipher = None
hiddenimports = collect_submodules('PyQt5')
hiddenimports += ['openpyxl','openpyxl.cell','openpyxl.styles','openpyxl.utils',
                  'openpyxl.workbook','openpyxl.worksheet','openpyxl.writer','openpyxl.reader']
datas = collect_data_files('openpyxl')
datas += [('src/otel_icon.png', '.')]
a = Analysis(['src/main.py'], pathex=['.'], binaries=[], datas=datas,
    hiddenimports=hiddenimports, hookspath=[], runtime_hooks=[],
    excludes=['matplotlib','numpy','pandas','scipy','PIL','tkinter'],
    cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='OtelKayit',
    debug=False, strip=False, upx=True, console=False, icon='otel.ico')
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name='OtelKayit')

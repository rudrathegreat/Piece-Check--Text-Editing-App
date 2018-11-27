# -*- mode: python -*-

block_cipher = None


a = Analysis(['PieceCheck.py'],
             pathex=['D:\\work\\Piece_Check\\Piece_Check\\File_Management\\Management.py:C:\\Users\\s72566\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages', 'D:\\work\\Piece_Check\\Piece_Check'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PieceCheck',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

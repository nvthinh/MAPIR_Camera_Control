# -*- mode: python -*-

block_cipher = None


a = Analysis(['MAPIR_Camera_Control.py'],
             pathex=['C:\\Users\\peau\\Desktop\\Kernel_Interface'],
             binaries=[('FreeImage.dll', '.'), ('FreeImagePlus.dll', '.'), ('opencv_aruco320.dll', '.'), ('opencv_aruco320d.dll', '.'), ('opencv_calib3d320.dll', '.'), 
             ('opencv_calib3d320.dll', '.'),
             ('opencv_core320.dll', '.'),
             ('opencv_core320d.dll', '.'),
             ('opencv_features2d320.dll', '.'),
             ('opencv_flann320.dll', '.'),
             ('opencv_imgcodecs320.dll', '.'),
             ('opencv_imgproc320.dll', '.')],
             datas=[('exiftool.exe', '.'), ('dcraw.exe', '.'), ('FiducialFinder.exe', '.'), ('Mapir_Converter.exe', '.'),
             ('instring.txt', '.'),('calib.txt', '.'), 
             ('MAPIR_Processing_dockwidget_base.ui', '.'),
             ('MAPIR_Processing_dockwidget_CAN.ui', '.'),
             ('MAPIR_Processing_dockwidget_modal.ui', '.'),
             ('MAPIR_Processing_dockwidget_time.ui', '.'),
             ('MAPIR_Processing_dockwidget_delete.ui', '.'),
             (('_gdal.pyd'),'.')],
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
          name='MAPIR_Camera_Control',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\peau\\Desktop\\corn_logo_color_square_256x256.ico')

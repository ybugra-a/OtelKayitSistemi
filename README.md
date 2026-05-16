Hotel Registration and Room Management System
Installation and Compilation Guide
FOLDER STRUCTURE
OtelKayit/
  src/                    ← Python source codes
    main.py
    data_manager.py
    kayit_modulu.py
    aktif_musteri_paneli.py
    oda_durumu_paneli.py
    arama_arsiv.py
    ayarlar.py
    styles.py
  OtelKayit.spec          ← PyInstaller configuration
  setup.iss               ← Inno Setup installation script
  build.bat               ← Automatic compilation script
  requirements.txt        ← Python dependencies
  README.md               ← This file
STEP 1 - INSTALL PYTHON
Go to https://python.org/downloads

Click the "Download Python 3.x.x" button.

During installation, make sure to check the "Add Python to PATH" box.

Complete the installation.

Control: You should see the version number when you type python --version in the command prompt.

STEP 2 - INSTALL INNO SETUP
Go to https://jrsoftware.org/isdl.php

Download "Inno Setup 6.x.x".

Install it with the default settings.

STEP 3 - COMPILE (ONE-CLICK)
Copy this folder to a location (e.g., C:\OtelKayitBuild\).

Double-click the build.bat file.

A black command window will open; follow the processes.

When finished, dist\installer\OtelKayitKurulum.exe will be created.

STEP 4 - INSTALL ON THE TARGET COMPUTER
Copy the OtelKayitKurulum.exe file to a USB flash drive.

Run it from the USB drive on the target computer.

Follow the installation wizard.

When finished, a shortcut named "Otel Kayit Sistemi" will appear on the desktop.

FIRST USE
When the application opens for the first time, the folder structure C:\OtelKayit\ is automatically created.

Add rooms from the Settings tab (e.g., 101, 102, 103, etc.).

Enter the first customer registration using the registration form.

DATA BACKUP
C:\OtelKayit\data\kayitlar.xlsx contains all the data.

Take a backup using the Settings > "Backup Now" button.

The application will show a reminder at startup every 30 days.

TROUBLESHOOTING
"Python not found" error:

Reinstall Python and make sure to check the "Add to PATH" option.

"Inno Setup not found" warning:

Install Inno Setup and run build.bat again.

Alternatively, open the setup.iss file manually with Inno Setup and compile it.

PyQt5 import error:

Run this in the command prompt: pip install PyQt5 --force-reinstall

Excel file could not be opened:

Check if the C:\OtelKayit\data\ folder exists.

If another program is keeping the Excel file open, close it.

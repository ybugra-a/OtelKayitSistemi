STEP 1 - INSTALL INNO SETUP
Go to https://jrsoftware.org/isdl.php
Download "Inno Setup 6.x.x".

STEP 2 - COMPILE (ONE-CLICK)
Copy this folder to a location (e.g., C:\OtelKayitBuild\).
Double-click the build.bat file.
A black command window will open; follow the processes.
When finished, dist\installer\OtelKayitKurulum.exe will be created.

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

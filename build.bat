@echo off
title Otel Kayit - Build v0.4

echo.
echo ================================================
echo   OTEL KAYIT SISTEMI - DERLEME ARACI v0.4
echo ================================================
echo.

echo [1/5] Python kontrol ediliyor...
python --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Python bulunamadi!
    pause
    exit /b 1
)
python --version

echo.
echo [2/5] Kutuphane kurulumu...
pip install -r requirements.txt --quiet --disable-pip-version-check
if errorlevel 1 ( echo HATA: Kutuphane kurulumu basarisiz! && pause && exit /b 1 )
echo Kutuphaneler hazir.

echo.
echo [3/5] Eski build temizleniyor...
if exist "dist\OtelKayit" rmdir /s /q "dist\OtelKayit"
if exist "build\OtelKayit" rmdir /s /q "build\OtelKayit"
if not exist "dist\installer" mkdir "dist\installer"

echo.
echo [4/5] PyInstaller derleniyor... (2-5 dakika)
pyinstaller OtelKayit.spec --noconfirm --clean
if errorlevel 1 ( echo HATA: PyInstaller basarisiz! && pause && exit /b 1 )
if not exist "dist\OtelKayit\OtelKayit.exe" ( echo HATA: exe olusturulamadi! && pause && exit /b 1 )
echo Derleme tamam.

echo.
echo [5/5] Inno Setup...
set ISCC=""
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" set ISCC="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
if exist "C:\Program Files\Inno Setup 6\ISCC.exe" set ISCC="C:\Program Files\Inno Setup 6\ISCC.exe"

if %ISCC%=="" (
    echo UYARI: Inno Setup bulunamadi.
    echo PyInstaller ciktisi hazir: dist\OtelKayit\
    pause
    exit /b 0
)
%ISCC% setup.iss
if errorlevel 1 ( echo HATA: Inno Setup basarisiz! && pause && exit /b 1 )

echo.
echo TAMAMLANDI: dist\installer\OtelKayitKurulum.exe
explorer dist\installer
pause

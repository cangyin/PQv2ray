@echo off
rmdir /s /q dist

echo ----------- Building package -----------
pyinstaller -F main.py ^
    -n pqv2ray ^
    --noupx 

echo ----------- Copy additional files -----------
xcopy /S components\config dist\components\config\
xcopy /S templates dist\templates\
xcopy /S ui\style.qss dist\ui\

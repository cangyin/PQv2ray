@echo off
rmdir /s /q dist

echo ----------- Building package -----------
if defined CI (
    set arg_windowed=--windowed
) else (
    set arg_windowed=
)

pyinstaller -F pqv2ray.py ^
    -n pqv2ray ^
    --icon resources\app-icon.ico ^
    %arg_windowed% ^
    --noupx 


echo ----------- Copy additional files -----------
xcopy /S components\config dist\components\config\
xcopy /S templates dist\templates\
xcopy /S ui\juniper.qss dist\ui\

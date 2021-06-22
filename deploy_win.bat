@echo off
rmdir /s /q dist

echo ----------- Building package -----------
if defined CI (
    pyinstaller -F pqv2ray.py ^
        -n pqv2ray ^
        --windowed ^
        --noupx 
) else (
    pyinstaller -F pqv2ray.py ^
        -n pqv2ray ^
        --noupx 
)

echo ----------- Copy additional files -----------
xcopy /S components\config dist\components\config\
xcopy /S templates dist\templates\
xcopy /S ui\style.qss dist\ui\

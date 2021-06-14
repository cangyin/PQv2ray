rmdir /s /q dist
pyinstaller -F main.py  --noupx --windowed

md dist\results
md dist\ui
copy config.json dist\
xcopy /s templates dist\templates\
xcopy /s components\config dist\components\config\
copy ui\style.qss dist\ui\

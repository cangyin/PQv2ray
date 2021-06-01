rmdir /s /q dist
pyinstaller -F main.py  --noupx --windowed

md dist\results
md dist\ui
copy config.json dist\
xcopy /s templates dist\templates\
copy ui\style.qss dist\ui\

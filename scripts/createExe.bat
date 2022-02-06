@echo off

pyinstaller -F -w --icon="resources/images/icon.ico" main.py
xcopy /E .\resources\ .\dist\resources\
xcopy /E .\conf\ .\dist\conf\
mkdir .\dist\logs
@echo off

pyinstaller -F -w --icon="resources/images/icon.ico" main.py
mkdir .\dist\resources
mkdir .\dist\conf
xcopy /E .\resources\ .\dist\resources\
xcopy /E .\conf\ .\dist\conf\
mkdir .\dist\logs
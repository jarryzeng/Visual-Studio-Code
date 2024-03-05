@echo off
call "pull command.bat"

call "E:\Microsoft VS Code\Code.exe"
tasklist /fi "imagename eq code.exe"

call "auto update.bat"
pause
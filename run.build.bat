@echo off
python build.py py2exe -d "compile/"
cd compile
rmdir /s /q build
pause&exit
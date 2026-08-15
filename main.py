import os
import socket
import threading
import requests

PANEL_URL = "https://astralnodes.net"
SERVER_ID = "20431082"
API_KEY = os.environ.get('ASTRAL_API_KEY') 

def encender_servidor():
    print("[BOT] ¡Conexión detectada! Enviando señal de encendido...")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    url = f"{PANEL_URL}/api/client/servers/{SERVER_ID}/power"
    data = {"signal": "start"}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in:
            print("[BOT] ¡Señal enviada con éxito!")
        else:
            print(f"[BOT] Error en la API: {response.status_code}")
    except Exception as e:
        print(f"[BOT] Falló la conexión: {e}")

def escuchar_minecraft():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 25565))
    server.listen(5)
    print("[BOT] Clon de Minecraft activo.")
    
    while True:
        client_socket, address = server.accept()
        threading.Thread(target=encender_servidor).start()
        client_socket.close()

if __name__ == "__main__":
    if not API_KEY:
        print("[ERROR] No se configuró la ASTRAL_API_KEY.")
    else:
        escuchar_minecraft()

import os
import socket
import threading
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

PANEL_URL = "https://astralnodes.net"
SERVER_ID = "20431082"
API_KEY = os.environ.get('ASTRAL_API_KEY') 

def encender_servidor():
    print("[BOT] ¡Conexión detectada! Enviando señal de encendido...")
    headers = {
        "Authorization": f"Bearer os.environ.get'ASTRAL_API_KEY'",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    url = f"https://astralnodes.net/api/client/servers/20431082/power"
    data = {"signal": "start"}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in [200, 201, 204]:
            print("[BOT] ¡Señal enviada con éxito!")
        else:
            print(f"[BOT] Error en la API: {response.status_code}")
    except Exception as e:
        print(f"[BOT] Falló la conexión: {e}")

def escuchar_minecraft():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 25565))
    server.listen(5)
    print("[BOT] Clon de Minecraft activo en el puerto 25565.")
    while True:
        client_socket, address = server.accept()
        threading.Thread(target=encender_servidor).start()
        client_socket.close()

# Servidor web falso para que Render no tire error de despliegue
class FakeWebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Despertador Activo")

def iniciar_servidor_web():
    port = int(os.environ.get("PORT", 10000))
    web_server = HTTPServer(('0.0.0.0', port), FakeWebHandler)
    print(f"[BOT] Servidor web de Render activo en el puerto {port}")
    web_server.serve_forever()

if __name__ == "__main__":
    if not API_KEY:
        print("[ERROR] No se configuró la ASTRAL_API_KEY.")
    else:
        # Iniciamos los dos servidores a la vez usando hilos
        threading.Thread(target=iniciar_servidor_web, daemon=True).start()
        escuchar_minecraft()

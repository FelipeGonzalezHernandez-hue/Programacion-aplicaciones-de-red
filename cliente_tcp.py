import socket  # Indispensable

HOST = '100.77.143.84' # Tu IP de felipepc
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Intentando conectar al servidor en {HOST}...")
        s.connect((HOST, PORT))
        s.sendall(b"Hola Felipe, soy un Juan pablo te acabo de enviar un mensaje. Prueba de comunicacion TCP exitosa.")
        data = s.recv(1024)
    print(f"Respuesta del servidor: {data.decode()}")
except Exception as e:
    print(f"Error de conexión: {e}")
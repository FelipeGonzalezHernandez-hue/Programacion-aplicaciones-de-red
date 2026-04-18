import socket

HOST = '100.77.143.84' # Tu IP de felipepc
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    mensaje = b"Probando envio de datos via UDP (Sin conexion previa)"
    print(f"Enviando mensaje a {HOST}...")
    s.sendto(mensaje, (HOST, PORT))
    
    # Esperamos la respuesta
    data, server = s.recvfrom(1024)
    print(f"Respuesta del servidor: {data.decode()}")
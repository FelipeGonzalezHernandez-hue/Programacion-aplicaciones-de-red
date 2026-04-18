import socket

HOST = '0.0.0.0'
PORT = 65433  # Usamos un puerto diferente para no chocar con TCP

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"SERVIDOR UDP: Esperando mensajes en el puerto {PORT}...")
    
    # En UDP no hay 'accept', recibimos directamente
    data, addr = s.recvfrom(1024)
    print(f"¡Paquete recibido desde {addr}!")
    print(f"Contenido: {data.decode()}")
    
    # Respondemos al cliente
    s.sendto(b"Hola Juanpablo, recibi tu paquete UDP correctamente.", addr)
    print("Respuesta UDP enviada.")
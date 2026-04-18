import socket

# Usamos 0.0.0.0 para que escuche a través de la red de Tailscale
HOST = '0.0.0.0' 
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"SERVIDOR TCP: Esperando conexión de tu amigo en el puerto {PORT}...")
    
    conn, addr = s.accept()
    with conn:
        print(f"¡CONECTADO! Conexión establecida desde: {addr}")
        data = conn.recv(1024)
        print(f"Mensaje recibido del cliente: {data.decode()}")
        conn.sendall(b"Hola desde el servidor felipepc. Mensaje recibido correctamente.")
        print("Respuesta enviada. Cerrando conexión.")
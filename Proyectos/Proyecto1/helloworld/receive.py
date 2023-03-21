import socket

def receive_messages(message=None):
    # Creamos un socket y nos conectamos al servidor MOM
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))

    # Recibimos los mensajes enviados a través del servidor MOM
    if not message:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print('Mensaje recibido:', data.decode())
    else:
        client_socket.sendall(message.encode())

    # Cerramos la conexión
    client_socket.close()

if __name__ == '__main__':
    # Recibimos los mensajes enviados a través del servidor MOM
    receive_messages()

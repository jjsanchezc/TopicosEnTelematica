import socket
import requests

def send_message(message):
    
    # Creamos un socket y nos conectamos al servidor MOM
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))

    # Enviamos el mensaje al servidor MOM
    client_socket.sendall(message.encode())

    # Cerramos la conexión
    client_socket.close()

if __name__ == '__main__':
    # Enviamos un mensaje de prueba al servidor MOM
    send_message('Hola, mundo!')

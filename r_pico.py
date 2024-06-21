"""
This file contains all the code used to interface with the Raspberry Pi Pico W
over bluetooth
"""

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = "0.0.0.0"
port = 5000

s.bind((host_name, port))

s.listen(5)

print(f"listening on {host_name}:{port}")


def handle_client(client_socket: socket.socket):
    request = client_socket.recv(4092)

    print("received " + bytes(request))

    client_socket.send(b"Hello")

    client_socket.close()


while True:
    client, addr = s.accept()

    print("accepted connection from " + addr[0], addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()

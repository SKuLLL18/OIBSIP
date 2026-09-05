"""
Simple two-client chat server using sockets + threading.
Run this FIRST, then run client.py in two separate terminals.
"""

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"   # localhost
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)  # only accept 2 clients for this simple version

clients = []       # holds connected client sockets
usernames = []      # holds matching usernames

print(f"[STARTING] Server is listening on {HOST}:{PORT}")


def timestamp():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender_socket=None):
    """Send a message to every connected client except (optionally) the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception:
                pass


def handle_client(client_socket):
    """Runs in its own thread for each connected client."""
    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
            broadcast(message, sender_socket=client_socket)
    except ConnectionResetError:
        pass
    finally:
        # Client disconnected — clean up
        index = clients.index(client_socket)
        clients.remove(client_socket)
        username = usernames[index]
        usernames.remove(username)

        disconnect_msg = f"[{timestamp()}] {username} has left the chat."
        print(disconnect_msg)
        broadcast(disconnect_msg)
        client_socket.close()


def receive_connections():
    """Main loop — accepts new clients and spins up a thread for each."""
    while True:
        client_socket, address = server.accept()
        print(f"[NEW CONNECTION] {address} connected.")

        client_socket.send("USERNAME".encode("utf-8"))
        username = client_socket.recv(1024).decode("utf-8")

        usernames.append(username)
        clients.append(client_socket)

        join_msg = f"[{timestamp()}] {username} has joined the chat!"
        print(join_msg)
        broadcast(join_msg, sender_socket=client_socket)
        client_socket.send("Connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    receive_connections()

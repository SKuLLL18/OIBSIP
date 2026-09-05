"""
Chat client. Run server.py first, then run this in two separate terminals
to simulate two users chatting.
"""

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def timestamp():
    return datetime.now().strftime("%H:%M")


def receive():
    """Runs in the background, listening for incoming messages."""
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "USERNAME":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except Exception:
            print("[DISCONNECTED] Lost connection to the server.")
            client.close()
            break


def write():
    """Runs in the main thread, reading user input and sending messages."""
    while True:
        message = input("")
        if message.strip().lower() == "/quit":
            client.close()
            break
        full_message = f"[{timestamp()}] {username}: {message}"
        client.send(full_message.encode("utf-8"))


if __name__ == "__main__":
    username = input("Enter your username: ")

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write()

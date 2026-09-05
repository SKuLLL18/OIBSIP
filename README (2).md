# Chat Application (Python · Sockets · Threading)

**Track:** Python Programming — Task 5 (Beginner Tier)
**Objective:** A real-time, two-user command-line chat application built using raw TCP sockets and threading.

## How It Works

- `server.py` listens for incoming client connections on `localhost:5050`.
- Each connecting client is asked for a username, then handled in its own
  background thread (`threading`), so the server can serve multiple clients
  at once without blocking.
- `client.py` connects to the server, spawns a background thread to
  **receive** messages while the main thread stays free to **send** messages
  — this is what makes the chat feel real-time and bidirectional.
- Messages are timestamped (`[HH:MM] username: message`) before being
  broadcast to all other connected clients.
- When a client disconnects, the server detects it, removes them from the
  active client list, and notifies everyone else in the chat.

## Tech Stack

- Python 3
- `socket` (TCP/IP networking)
- `threading` (concurrent send/receive + multiple clients)
- `datetime` (message timestamps)

## How to Run

1. Start the server first:
   ```
   python3 server.py
   ```
2. In a **separate terminal**, start a client:
   ```
   python3 client.py
   ```
   You'll be prompted for a username.
3. Open a **second terminal** and run `client.py` again with a different
   username to simulate a second user.
4. Type messages and press Enter to send. Type `/quit` to disconnect.

## Feature Checklist (per task requirements)

- [x] Server script that listens for incoming client connections
- [x] Client script that connects to the server
- [x] Real-time, bidirectional message exchange between two connected clients
- [x] Messages displayed with a timestamp prefix (e.g. `[14:35] Alice: Hello`)
- [x] Graceful disconnection handling — other clients are notified when someone leaves
- [x] Both scripts runnable on the same machine using `localhost`

## Notes

- This is a **local, unencrypted** chat for learning purposes — not intended
  for use over the open internet without adding TLS/authentication.
- Only supports plain-text messages (no persistence, no chat rooms) — see the
  Advanced tier of this task for a GUI/multi-room/database-backed version.

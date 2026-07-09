import socket
ENCODING_FORMAT = "UTF-8"
HEADER = 64

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8002
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDR)

server.listen()
print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

conn, addr = server.accept()
print(f"Connection established with {addr}")

while True:
    msg_len = conn.recv(HEADER).decode(ENCODING_FORMAT)
    if msg_len:
        msg = conn.recv(int(msg_len)).decode(ENCODING_FORMAT)
        print(f"Message from client: {msg}")
        if msg == "end":
            conn.send('Disconnected from server'.encode(ENCODING_FORMAT))
            break
        else:
            print(f'A new message from client: {msg}')

            conn.send(f"Server received your message: {msg}".encode(ENCODING_FORMAT))

            


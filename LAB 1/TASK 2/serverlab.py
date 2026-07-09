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
        count = 0
        lower_msg = msg.lower()
        for i in range(int(len(lower_msg))):
          if lower_msg[i] in "aeiou":
                count += 1
         
    if msg == "end":
            conn.send('Disconnected from server'.encode(ENCODING_FORMAT))
            break
    else:
            print(f'A new message from client: {msg}')

             

    if count <= 0:
        conn.send(f"There are no vowels".encode(ENCODING_FORMAT))
    elif count <= 2:
        conn.send(f"Enough vowels I guess".encode(ENCODING_FORMAT))
    elif count > 2:
        conn.send(f"Too many vowels".encode(ENCODING_FORMAT))  

    


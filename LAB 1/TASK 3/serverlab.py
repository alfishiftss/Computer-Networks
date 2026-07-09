import socket
import threading

ENCODING_FORMAT = "UTF-8"
HEADER = 64

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8002
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Fixed typo here: setsockopt instead of setsocketopt
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind(SERVER_ADDR)

def clients(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        msg_len = conn.recv(HEADER).decode(ENCODING_FORMAT)
        if msg_len:
            msg = conn.recv(int(msg_len)).decode(ENCODING_FORMAT)
            
            if msg == "end":
                conn.send('Disconnected from server'.encode(ENCODING_FORMAT))
                break
                
            print(f"[{addr}] a new message from client: {msg}")

            count = 0
            lower_msg = msg.lower()
            
            for char in lower_msg:
                if char in "aeiou":
                    count += 1

            if count <= 0:
                conn.send("not enough vowels".encode(ENCODING_FORMAT))
            elif count <= 2:
                conn.send("enough vowels i  guess".encode(ENCODING_FORMAT))
            else:
                conn.send("too many vowels".encode(ENCODING_FORMAT))
                
     
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

def start():
    server.listen()
     
    print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=clients, args=(conn, addr))   
        thread.start()
        # This active count print belongs inside the while loop
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

 
print("[Starting] server is starting...")
start()
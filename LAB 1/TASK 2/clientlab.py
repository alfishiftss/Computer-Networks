import socket
ENCODING_FORMAT = "UTF-8"
HEADER = 64

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8002
SERVER_ADDR = ( SERVER_IP, SERVER_PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)

def send_message(message):
    msg_len = str(len(message))
    encoded_msg_len = msg_len.encode(ENCODING_FORMAT)
    encoded_padded_string = b" "*(HEADER-len(encoded_msg_len))

    final_msg_len = encoded_msg_len+ encoded_padded_string
    client.send(final_msg_len)

    client.send(message.encode(ENCODING_FORMAT))

    server_msg = client.recv(2048).decode(ENCODING_FORMAT)
    print(f"Server: {server_msg}")


while True:
    message = input("Enter your message: ")
    send_message(message)
    if message == "end":
        break
    
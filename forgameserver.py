import socket
import threading

HOST = '127.0.0.1'
PORT = 12345



def handle_client(client):
    pass

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server started on {HOST}:{PORT}")
    
    except socket.error as msg:
        print(f"Socket error: {msg}")
        exit(1)

if __name__ == "__main__":
    start_server()

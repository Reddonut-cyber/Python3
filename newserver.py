import threading
import socket

host = '127.0.0.1'
port = 21002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
names = []

def broadcast(message):
    for client in clients:
        client.send(message)
        
def handle(client):
    while True:
        try:
            message = client.recv(32).decode()
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = name[index]
            broadcast(f'{name} left the chat'.encode())
            names.remove(name)
            break
        
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send("NICK".encode())
        name = client.recv(32).decode()
        names.append(name)
        clients.append(client)
        
        print(f'Name of the client is {name}')
        broadcast(f'{name} joined the chat'.encode())
        client.send('connected to the server'.encode())
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
print("server is listening")
receive()
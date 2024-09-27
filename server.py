import socket
import threading
import os

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received: {message}")
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()
    clients.remove(client_socket)

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message: {e}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Server started on port 9999. Use serveo.net to forward this port.")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def setup_port_forwarding():
    # Command to establish port forwarding using serveo.net
    os.system("ssh -R 9999:localhost:9999 serveo.net")

if __name__ == "__main__":
    setup_port_forwarding()  # Automatically set up port forwarding
    start_server()

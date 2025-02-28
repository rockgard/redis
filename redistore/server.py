import socket
import threading

def handle_client(conn, addr):
    """ Handlesnthe client connection"""
    print(f"Client Connected on IP address : {addr}")

    try:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break #Client disconnected
            print(f"Recieved : {data}")
            response = "PONG\n" if data.upper() == "PING" else "ERROR: Unknown command\n"
            conn.sendall(response.encode()) # send response
    
    finally:
        conn.close()
        print(f"Client disconnected : {addr}")

def start_server():
    """Starts TCP server """
    HOST, PORT = "127.0.0.1", 6379  ##localhost and redis default port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()  # Start listening for connections
        print(f"Server listening on {HOST}:{PORT}")

        while True: 
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()

    



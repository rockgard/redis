import socket

HOST, PORT = "127.0.0.1", 6379

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        response = s.recv(1024).decode()
        return response

if __name__ == "__main__":
    while True:
        cmd = input("> ")
        if cmd.lower() in ["exit", "quit"]:
            break
        print(send_command(cmd))

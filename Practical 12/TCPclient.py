
import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        a=input("Client msg:")
        if(a=="end"):
            print("Session Terminated.")
            break
        s.sendall(a.encode())
        data = s.recv(1024)
        print(f"Server msg:",data)
    s.close()

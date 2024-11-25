import socket

HOST = "127.0.0.1"
PORT = 65432

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
while True:
    data = conn.recv(1024)            
    if not data:
        print("Session Terminated.")
        break
    print("Client msg:",data)
    str=input("Server msg:")
    conn.sendall(str.encode())
conn.close()
s.close()

import socket
import time
import sys

port=12345

def ping_server(host):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.settimeout(2)
            start = time.time()
            s.sendto(b'Ping', (host, port))
            data, addr = s.recvfrom(1024)
            end = time.time()
            print(f"Received {data.decode()} from {addr} in {end - start:.2f} seconds")
        except socket.timeout:
            print("Request timed out")

if __name__ == "__main__":
    ping_server(sys.argv[1])

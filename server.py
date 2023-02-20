import socket
import sys
import time, threading

def connect_Thread(addr, port_no):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (addr, port_no)
    sock.settimeout(0)
    sock.setblocking(1)
    result = -1
    while result != 0:
        result = sock.connect_ex(server_address)
    try:
        msg = b'this is my message'
        sock.sendall(msg)
    finally:
        sock.close()
    

print("Starting server connections!\n")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port1 = 0
port2 = 0
if len(sys.argv) > 2:
    port1 = int(sys.argv[1])
    port2 = int(sys.argv[2])
    print(port1, port2)
else:
    exit()
server_address = ('0.0.0.0', port1)
sock.bind(server_address)
sock.listen(1)
print("My socket is set up and waiting for another server!\n")
while True:
    print("Waiting for connection")
    x = threading.Thread(target=connect_Thread, args=('192.168.0.143', port2), daemon=True)
    x.start()
    connection, client_addr = sock.accept()
    try:
        data = connection.recv(4096)
        if data:
            print("This is the data I received:", data.decode())
    finally:
        connection.close()
    time.sleep(3)
        
        

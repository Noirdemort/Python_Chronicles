import socket
import time

host = '127.0.0.1'
port = 8000

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))
sock.setblocking(0)

quitting = False
print("Server started")

while not quitting:
    try:
        data, addr = sock.recvfrom(1024)
        if 'Quit' in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)

        print("{} :: {} :: {}".format(  time.ctime(time.time()) ,str(addr), str(data) ) )

        for client in clients:
            sock.sendto(data,client)
    
    except:
        pass

sock.close()


import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8000))
sock.listen(1)
# no. of servers accepted

connections = []

def handler(c,a):
        while True:
            data = c.recv(1024)
            for connection in connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ":" + str(a[1]),"disconnected" )
                connections.remove(c)
                c.close()
                break

while True:
    c,a = sock.accept()
    connections.append(c)
    cThread = threading.Thread(target=handler,args=(c,a))
    cThread.daemon = True
    cThread.start()
    print(connections)
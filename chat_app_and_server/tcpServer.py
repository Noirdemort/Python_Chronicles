import socket

def Server():
    host = '127.0.0.1'
    port = 5000

    sock = socket.socket()
    sock.bind((host,port))
    sock.listen(1)

    c,addr = sock.accept()
    print(str(addr))

    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from user",str(data))
        str(data).upper()
        print("sending data",data)
        c.send(data)
    c.close()

if __name__=='__main__':
    Server()
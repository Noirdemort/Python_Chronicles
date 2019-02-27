import socket

def Client():
    host = '127.0.0.1'
    port = 5000

    sock = socket.socket()
    sock.connect((host,port))

    msg = input("---->")
    
    while msg != 'o0':

        sock.send(bytes(msg,'utf-8'))
        msg = sock.recv(1024)

        # data = sock.recv(1024)
        # sock.send(bytes(data,'utf-8'))

        print(str(msg))
        msg = input("---->")
    sock.close()

if __name__=='__main__':
    Client()
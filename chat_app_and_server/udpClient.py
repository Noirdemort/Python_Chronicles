import socket

def Client():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1',5000)

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))

    msg = input("---->")
    
    while msg != 'o0':
        msg = bytes(msg,'utf-8')
        sock.sendto(msg,server)
        data, addr = sock.recvfrom(1024)
        print("Recievced from server: {}".format(data))
        msg = input("---->")
    sock.close()

if __name__=='__main__':
    Client()
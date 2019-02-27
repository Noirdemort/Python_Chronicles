# udp stands for user datagram protocol
# it is unreliable connectionless protocol
# sort of broadcasting rather than one on one 

import socket

def Server():
    host = '127.0.0.1'
    port = 5000

    sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))

    print("Service started...")
    while True:
        data, addr = sock.recvfrom(1024)
        print("Message from user {}".format(str(addr)))
        print("Data: {}".format(str(data)))
        data.upper()
        print("Sending data: {}".format(data))
        sock.sendto(data,addr)
    sock.close()

if __name__=='__main__':
    Server()
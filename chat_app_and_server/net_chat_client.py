import time
import socket
import threading

tLock = threading.Lock()
shutdown = False 

def recieving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            tLock.release()
    
host = '127.0.0.1'
port = 0

server = ('127.0.0.1',8000)

sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))
sock.setblocking(0)

rT = threading.Thread(target=recieving,args = ('RecvThread',sock))
rT.start()

alias = input("Alias: ")
msg = input("Message: ")
while msg != 'o':
    if msg != '':
        sock.sendto(bytes(alias +': '+ msg,'utf-8'), server)
        tLock.acquire()
        msg = input("Message: ")
        tLock.release()
        time.sleep(0.5)

shutdown = True
rT.join()
sock.close()


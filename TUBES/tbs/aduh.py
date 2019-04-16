import socket
import time
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ipserver = 'localhost'
port = 48666

sock.connect((ipserver,port))

try:
    while True:
        try:
            data = sock.recv(6000)
            print data
            time.sleep(1)
        except:
            break
    
finally:
    sock.close()
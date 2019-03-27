import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_addres = 'localhost'

port_number = 50000

reciver_addres = (ip_addres,port_number)

sock.bind(reciver_addres)

print'waiting for something...'

data, transmit_addr = sock.recvfrom(1024)

print 'has received : ',data,' from ',transmit_addr

sock.close
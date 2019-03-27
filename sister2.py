import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = 'fajar 1301164476'

ip_addres = 'localhost'

port_number = 50000

receiver_address = (ip_addres,port_number)

sock.sendto(data,receiver_address)

print 'sent to ',data,' to ',receiver_address
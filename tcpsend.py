import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

data = 'haloo'

ip_addres = 'localhost'

port_number = 10000

receiver_address = (ip_addres,port_number)
sock.connect(receiver_address)
for i in range(1,3):
    x = raw_input('chat : ')
    sock.send(x)
    sock.connect(receiver_address)


print 'sent to ',data,' to ',receiver_address
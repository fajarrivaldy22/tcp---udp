import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

data = 'fajar ganteng 1301164476'

ip_addres = '10.20.198.69'

port_number = 50001

receiver_address = (ip_addres,port_number)

sock.connect(receiver_address)

for i in range(1,4):
    sock.send(data)

print 'sent to ',data,' to ',receiver_address
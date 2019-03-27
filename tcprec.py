import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_number = 'localhost'
port_number = 50001

receiver_addres = (ip_number,port_number)

sock.bind(receiver_addres)

sock.listen(1)

print 'waiting for a connection...'

conn , sender_ddr = sock.accept()

data = conn.recv(1024)

print 'has received : ',data,' from ',sender_ddr

conn.close()
sock.close()

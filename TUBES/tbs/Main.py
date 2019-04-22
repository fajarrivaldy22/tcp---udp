import socket
import json,urllib
import time
import threading

url = 'https://indodax.com/api/btc_idr/trades'
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ipserver = 'localhost'
port = 48666

sock.bind((ipserver,port))
print("socket di bind ke %s port %d" % (ipserver,port))

sock.listen(5)
connections = []

def getconnection():
    while True:
        connection, address = sock.accept()
        connections.append(connection)
        print('koneksi dari',address)


temp = 0

t = threading.Thread(target=getconnection,args=())
t.start()
while True:

    
    try:
        while True:
            try:
                response = urllib.urlopen(url)
                data = json.loads(response.read())
                if((data[0]['tid']!=temp)  ): 
                    for conn in connections:
                        conn.sendall(str('transaksi id: '+data[0]['tid']+', price: '+data[0]['price']))
                    temp = data[0]['tid']
                time.sleep(2)
            except:
                break
    finally:
        connection.close()


    ##response = urllib.urlopen(url)
    ##data = json.loads(response.read())
    ##if((data[0]['tid']!=temp)  ): 
        #sock.send('halo')
    ##    temp = data[0]['tid']
    ##time.sleep(2)
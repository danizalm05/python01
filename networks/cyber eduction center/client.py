import socket

'''
https://cyber.org.il/data/  page 40   2.1
run 'server.py' before running  this program 

nslookup  networks.cyber.org.il ===> ip= 213.57.2.5
 
python -V    python version:   Python 3.6.4 :: Anaconda, Inc.
http://www.lamed-oti.com/school/rs/networks/
 
 
'''
my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 8820))
cmd = input("Your command? ")
my_socket.send(cmd.encode())# encode:  turn type string to type bytes '


data = my_socket.recv(1024).decode()# decode opposite to encode
print ('The server sent: ' + (data))
my_socket.close()
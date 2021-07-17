import socket

'''nslookup  networks.cyber.org.il ===> ip= 213.57.2.5
http://cyber.org.il/
python -V    python version:   Python 3.6.4 :: Anaconda, Inc.
http://www.lamed-oti.com/school/rs/networks/
download 'echo_server_stream.pyc'
run: python  echo_server_stream.pyc
'''
my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 8820))
cmd = input("Your command? ")
#msg = "Hell"
my_socket.send(cmd.encode())


data = my_socket.recv(1024).decode()
print ('The server sent: ' + (data))
my_socket.close()
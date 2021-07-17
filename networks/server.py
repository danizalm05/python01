import socket
server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 8820))# bind the socket to host and port
server_socket.listen(1) #1 == so that it will perpetually listen till we close the connection
(client_socket, client_address) = server_socket.accept()
print ("Connection from: " + str(client_address))
client_name = client_socket.recv(1024).decode()
print ('client_name = ', str(client_name))
s = 'Hello '  + str(client_name)
print (s)
client_socket.send(s.encode())
client_socket.close()

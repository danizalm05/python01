#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition  page 24
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network
#  

# UDP client and server on localhost
#  The sever write a message from the client 
#  the client send a message to the server
'''

1. run the server  from a consol  ' python udp_remote.py server ""
 specifying the server IP address as the empty string  means
      “any local interface”
  output: 
      Namespace(role='server', host='', p=1060)
      Server Listening at ('0.0.0.0', 1060)  
      
2. run client  from another consol  'python udp_remote.py client guinness' 
  twice
output
 consol 1  Server:  
   

  consol 2 Client:
    
   
    
'''

import argparse, socket
from datetime import datetime
MAX_BYTES = 65535 



'''
Server randomly chooses to answer only half of the requests, which will let
you see how to build reliability into your client code without waiting
what might be hours for a real dropped packet to occur on your network.
'''
def  server(interface, port):
 
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 sock.bind((interface, port))
 print('Server Listening at', sock.getsockname())
 while True:
     data, address = sock.recvfrom(MAX_BYTES)
     #if random.random() > 2:
     #    print('Pretending to drop packet from {}'.format(address))
     #    continue
     text = data.decode('ascii')
     print('The client at {} says {!r}'.format(address, text))
     message = 'Your data was {} bytes long'.format(len(data))
     sock.sendto(message.encode('ascii'), address) 

def  client(hostname, port): 
  print(hostname) 
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #hostname = sys.argv[2]
  sock.connect((hostname, port))
  print('Client socket name is {}'.format(sock.getsockname()))
  delay = 0.1 # seconds
  text = 'This is another message'
  data = text.encode('ascii') 
  while True:
    sock.send(data)
    print('Waiting up to {} seconds for a reply'.format(delay))
    sock.settimeout(delay)
    try:
      data = sock.recv(MAX_BYTES)
    except socket.timeout:
       delay *= 2 # wait even longer for the next request
       if delay > 2.0:
          raise RuntimeError('I think the server is down')
    else:
       break # we are done, and can stop looping


  print('The server says {!r}'.format(data.decode('ascii')))

if __name__ == '__main__':
 choices = {'client': client, 'server': server}
 parser = argparse.ArgumentParser(description='Send and receive UDP,'
   ' pretending packets are often dropped')  
 parser = argparse.ArgumentParser(description='Send and receive UDP,'
    ' pretending packets are often dropped')
 parser.add_argument('role', choices=choices, help='which role to take')
 parser.add_argument('host', help='interface the server listens at;'
   'host the client sends to')
 parser.add_argument('-p', metavar='PORT', type=int, default=1060,
 help='UDP port (default 1060)')
 args = parser.parse_args()
 print (args) # Namespace(role='server', host='', p=1060)
 function = choices[args.role]
 function(args.host, args.p)
 
 
 
 

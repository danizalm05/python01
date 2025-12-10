#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_local.py
# Foundations of Python Network Programing - page 21

# UDP client and server on localhost
#  The sever write a message from the client 
#  the client send a message to the server
'''
1. run the server  from a consol  ' python udp_local.py server
2. run client  from another consol  'python udp_local.py client' 
  twice
output
 consol 1  Server:  
  Listening at ('127.0.0.1', 1060)
  After starting clinet twice you'll get the next two messages  :
   The client at ('127.0.0.1', 46056) says 'The time is 2014-06-05 10:34:53.448338'
   The client at ('127.0.0.1', 39288) says 'The time is 2014-06-05 10:34:54.065836'

  consol 2 Client:
   $ python udp_local.py client
   The OS assigned me the address ('0.0.0.0', 46056)
   The server ('127.0.0.1', 1060) replied 'Your data was 46 bytes long'

   $ python udp_local.py client
   The OS assigned me the address ('0.0.0.0', 39288)
   The server ('127.0.0.1', 1060) replied 'Your data was 46 bytes long'  
    
'''

import argparse, socket
from datetime import datetime
MAX_BYTES = 65535 

def server(port):
    
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
 # AF_INET:Internet family of protocols, and it is of SOCK_DGRAM 
 # datagram type,  which means it will use UDP on an IP network
  
 sock.bind(('127.0.0.1', port))
 # This step fails if another program is already using that UDP port 
 # So you can run using a '–p' option to select a different port number
 
 s = sock.getsockname()
 # getsockname(): method to retrieve a tuple that contains
 # the current IP address and port to which the socket is bound.
 print('Listening at {}'.format(s))   
 #  .format() method  embedding variables or values into placeholders within a template string.
 while True:
     
   data, address = sock.recvfrom(MAX_BYTES)
   text = data.decode('ascii')#convert bytes object into a string using 'ascii''
   print('The client at {} says {!r}'.format(address, text))
   #{!r} shows the full structure, including quotes and escape characters.
   
   text = 'Your data was {} bytes long'.format(len(data))
   data = text.encode('ascii')
   sock.sendto(data, address) 

def client(port): 
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   text = 'The time is {}'.format(datetime.now())
   data = text.encode('ascii')
   sock.sendto(data, ('127.0.0.1', port))
   print('The OS assigned me the address {}'.format(sock.getsockname()))
   data, address = sock.recvfrom(MAX_BYTES) # Danger!
   text = data.decode('ascii')
   print('The server {} replied {!r}'.format(address, text))
 
if __name__ == '__main__':
 choices = {'client': client, 'server': server}
 parser = argparse.ArgumentParser(description='Send and receive UDP locally')
 parser.add_argument('role', choices=choices, help='which role to play')
 parser.add_argument('-p', metavar='PORT', type=int, default=1060,
 help='UDP port (default 1060)')
 args = parser.parse_args() # Namespace(role='server', p=1060)

 action = choices[args.role] # args.role ==>  'client' or 'server' 
 # (function) ==> <function server at 0x000001EFB797D580>
 # type(function) ==> <class 'function'>
 # args.p ==> 1060
 action(args.p)
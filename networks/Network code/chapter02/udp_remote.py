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
 specifying the server IP address as the empty string  means “any local interface”
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
  

def  client(hostname, port): 
 
  print('Client')     

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
 
 
 
 

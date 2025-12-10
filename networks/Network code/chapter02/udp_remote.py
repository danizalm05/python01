#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition  page 24
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network
#  

# UDP client and server on localhost
#  The sever write a message from the client 
#  the client send a message to the server
'''
1. run the server  from a consol  ' python udp_local.py server
2. run client  from another consol  'python udp_local.py client' 
  twice
output
 consol 1  Server:  
   

  consol 2 Client:
   $ python udp_local.py client
   
    
'''

import argparse, socket
from datetime import datetime
MAX_BYTES = 65535 

def server(port):
   

def client(port): 
    
  
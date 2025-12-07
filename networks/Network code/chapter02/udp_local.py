#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_local.py
# Foundations of Python Network Programing - page 21

# UDP client and server on localhost


import argparse, socket
from datetime import datetime
MAX_BYTES = 65535 

def server(port):
 print("Server")

def client(port): 
 print("Client")   
 
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
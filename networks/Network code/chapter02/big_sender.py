
#!/usr/bin/env python3
# Sending a Large UDP Packet
# Foundations of Python Network Programming, Third Edition  page 32
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/big_sender.py
# Send a big UDP datagram to learn the MTU of the network path.

# This is the internet version nd it works only on linux


import argparse, socket, sys

# Inlined constants, because Python 3.6 has dropped the IN module.

class IN:
    IP_MTU = 14
    IP_MTU_DISCOVER = 10
    IP_PMTUDISC_DO = 2

if sys.platform != 'linux':
    print('Unsupported: Can only perform MTU discovery on Linux',
          file=sys.stderr)
    sys.exit(1)
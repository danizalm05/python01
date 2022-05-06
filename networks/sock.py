# How to find the IP of TOR
#https://www.youtube.com/watch?v=fDeLtKUxTmM   3:12:00  03:13:00
import socks   # install  pysocks
import socket
import requests
'''
netstat -n   display active connections  IP  and port number  
netstat -a   All active and inactive connections and  TCP and UDP ports the device is  listening.
netstat -b   lists all the executables (applications) associated with each connection.


How to find the port of TOR:

1.  Run TOR
    Run Task Manager
    find  PID number of TOR
   
2. Run  netstat -aon
     Find the line with the PID of step 1 with state LISTENING
     The port in that line is the TOR  port    
'''
r0= requests.get("http://icanhazip.com/")
print("Regular IP = ",r0.content)

socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",9150 ) #This is the tor port form stem 2
socket.socket = socks.socksocket
#print(socket.socket)
r= requests.get("http://icanhazip.com/")
print("IP of TOR = ",r.content)


#  127.0.0.1:9150         0.0.0.0:0              LISTENING       12188
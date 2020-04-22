'''
Created on Apr 22, 2020

@author: aron
'''
import socket
Host = input("What is the host name? (The other program should have given it to you)")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(Host == ""):
    sock.connect((socket.gethostname(), 1234))
else:
    sock.connect((Host, 1234))
msg = sock.recv(1024)
print(msg.decode("utf-8"))
sock.close()

'''
Created on Apr 22, 2020

@author: aron
'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))

msg = sock.recv(1024)
print(msg.decode("utf-8"))
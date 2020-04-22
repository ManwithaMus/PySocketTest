'''
Created on Apr 22, 2020

@author: aron
'''
import socket

   
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 1234))
sock.listen(3)

while True:
    clientsocket = sock.accept()
    address = sock.accept()
    print(f"The Ip connecting to is {address}!")
    clientsocket.send(bytes("Hello Gordan!", "utf-8"))
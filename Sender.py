'''
Created on Apr 22, 2020

@author: aron
'''
import socket
text = input("What do you want to send over?\n")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("The socket host name should be: "+socket.gethostname())
sock.bind((socket.gethostname(), 1234))
sock.listen(1)

print("Waiting for connection!")
clientsocket, address = sock.accept()
print("Connection has been established")
clientsocket.send(bytes(text, "utf-8"))
sock.close()
'''
Created on Apr 22, 2020

@author: aron
'''
import socket
class server:
   
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((socket.gethostname(), 1234))
    sock.listen(3)

    while True:
        clientsocket = sock.accept()
        address = sock.accept()
        check = "No errors so far and "+ address + " has connected safely!"
        print(check)
        print("working?")
        clientsocket.send("You should be connected to the server!")
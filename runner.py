'''
Created on Apr 22, 2020

@author: aron
'''
import main
import client

m = main()
c = client() 

 
def start():
    print("This is running!")
    m.server
    c.client
    print(m.check)
    print(c.msg)
start()   
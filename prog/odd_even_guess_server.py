#!/usr/bin/python -u
import random
import os
import socket              
import thread
import datetime

s = socket.socket() 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)       
host = "192.168.1.6" 
port = 2525          
print 'Server started!'
print 'Waiting for clients...'
s.bind((host, port))        
s.listen(5)                 
random.seed(os.getuid())
def isItInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def check_rand(nbr,lucky_type,clientsocket):
	rand = random.randrange(0,100)
	clientsocket.send('My rand is: '+str(rand)+'\n')
	if (int(nbr)+rand)%2==0 and lucky_type== 2:
		return True 
	elif (int(nbr)+rand)%2!=0 and lucky_type== 1:
		return True
	else:
		return False
def on_new_client(clientsocket,addr):
    Try = 4
    win = 50
    while True:
        clientsocket.send("Welcome to our odd even game\n To start you need to choose your lucky type:")
        lucky_type = 5
        while lucky_type != 1 and lucky_type != 2:
          clientsocket.send("\n1)odd\n2)even\n>>")
          try:
            lucky_type = int(clientsocket.recv(256))
            print str(datetime.datetime.now())+'::'+str(addr)+">>"+str(lucky_type)
          except Exception as e:
            pass
        while Try>0 and win > 0:
        	clientsocket.send("Give me a number: ")
        	nbr = clientsocket.recv(1024)
        	print str(datetime.datetime.now())+'::'+str(addr)+">>"+str(nbr)
        	while not isItInt(nbr):
        		clientsocket.send("it\'s not a valide number\nGive me a number: ")
        		nbr = clientsocket.recv(1024)
        		print str(datetime.datetime.now())+'::'+str(addr)+">>"+str(nbr)
        	if(check_rand(nbr,lucky_type,clientsocket)):
        		win -= 1
        		clientsocket.send('good Keep going :)\n')
        	else:
        		Try -= 1 
        		clientsocket.send('Try hard My boy :(\n'+str(Try)+' try left\n')
        if(Try==0):
        	clientsocket.send('I\'m sorry best luck for the next time\n')
        	clientsocket.close()
        elif Try>0 and win ==0:
        	clientsocket.send('Here is the flag: Bugs_Bunny{7chitou}\n')
        	clientsocket.close()
    clientsocket.close()
while True:
   c, addr = s.accept()     # Establish connection with client.
   thread.start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()
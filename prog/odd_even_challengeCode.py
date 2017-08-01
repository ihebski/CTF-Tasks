#!/usr/bin/python -u
import random
import os
import socket              
import thread

                
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


if __name__ == '__main__':
    Try = 4
    win = 100
    while True:
        clientsocket.send("Welcome to our odd even game\n To start you need to choose your lucky type:")
        lucky_type = 5
        while lucky_type != 1 and lucky_type != 2:
          clientsocket.send("\n1)odd\n2)even\n>>")
          try:
            lucky_type = int(clientsocket.recv(1024))
          except Exception as e:
            pass
        while Try>0 and win > 0:
        	clientsocket.send("Give me a number: ")
        	nbr = clientsocket.recv(1024)
        	print str(addr)+">>"+str(nbr)
        	while not isItInt(nbr):
        		clientsocket.send("it\'s not a valide number\nGive me a number: ")
        		nbr = clientsocket.recv(1024)
        	if(check_rand(nbr,lucky_type,clientsocket)):
        		win -= 1
        		clientsocket.send('Good Keep going :) \n'str(win)+' lucky rand left to win\n')
        	else:
        		Try -= 1 
        		clientsocket.send('Try hard My boy :(\n'+str(Try)+' try left\n')
        if(Try==0):
        	clientsocket.send('I\'m sorry best luck for the next time\n')
        	clientsocket.close()
        elif Try>0 and win ==0:
        	clientsocket.send('Here is the flag: ######')
        	clientsocket.close()
    clientsocket.close()

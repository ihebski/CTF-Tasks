#!/usr/bin/env python2

import socket
import threading
import time
import SocketServer
import random

HOST = "0.0.0.0"
PORT = 11222
WELCOME_MSG = "Hi, do YOU love math ?!?!\n"
ERROR_MSG = "check your input please\n"
CORRECT_MSG = "Great, keep it up\n"
WRONG_MSG = "Try again later!\n"
FLAG = "M4TH_LO0k!_HarD_But_s0_EA5Y\n"
MAX_TO_SOLVE = 500

capitals={
            "Washington":"Olympia","Oregon":"Salem",\
            "California":"Sacramento","Ohio":"Columbus",\
            "Nebraska":"Lincoln","Colorado":"Denver",\
            "Michigan":"Lansing","Massachusetts":"Boston",\
            "Florida":"Tallahassee","Texas":"Austin",\
            "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",\
            "Alaska":"Juneau","Utah":"Salt Lake City",\
            "New Mexico":"Santa Fe","North Dakota":"Bismarck",\
            "South Dakota":"Pierre","West Virginia":"Charleston",\
            "Virginia":"Richmond","New Jersey":"Trenton",\
            "Minnesota":"Saint Paul","Illinois":"Springfield",\
            "Indiana":"Indianapolis","Kentucky":"Frankfort",\
            "Tennessee":"Nashville","Georgia":"Atlanta",\
            "Alabama":"Montgomery","Mississippi":"Jackson",\
            "North Carolina":"Raleigh","South Carolina":"Columbia",\
            "Maine":"Augusta","Vermont":"Montpelier",\
            "New Hampshire":"Concord","Connecticut":"Hartford",\
            "Rhode Island":"Providence","Wyoming":"Cheyenne",\
            "Montana":"Helena","Kansas":"Topeka",\
            "Iowa":"Des Moines","Pennsylvania":"Harrisburg",\
            "Maryland":"Annapolis","Missouri":"Jefferson City",\
            "Arizona":"Phoenix","Nevada":"Carson City",\
            "New York":"Albany","Wisconsin":"Madison",\
            "Delaware":"Dover","Idaho":"Boise",\
            "Arkansas":"Little Rock","Louisiana":"Baton Rouge"
        }

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        try:
            self.request.sendall(WELCOME_MSG)
            num_solved = 0
            for level in range(1,MAX_TO_SOLVE+1):
                eq, res , ran = random.choice([self.rand_equation,self.random_quiz])()
                self.request.sendall("Level {}.: {}\n".format(str(level), eq))
                try:
                    answer = self.request.recv(1024)
                    if ran == "1":
                        answer = int(answer.strip())
                    elif ran == "2":
                        answer = answer.strip()
                except:
                    self.request.sendall(ERROR_MSG)
                    return
                
                if answer == res:
                    num_solved += 1
                    self.request.sendall(CORRECT_MSG)
                else:
                    self.request.sendall(WRONG_MSG)
                    return
            if num_solved == MAX_TO_SOLVE:
                self.request.sendall(FLAG)
        except:
            return

    def rand_equation(self):
        num1 = num2 = 0
        operators = ["*","+","-"]
        num_range = [2, 20*random.randint(10,150)]

        op = operators[random.randint(0, len(operators) -1)]

        while (num1 in [0,1]) or (num2 in [0,1]): 
            num1 = random.randint(num_range[0], num_range[1])
            num2 = random.randint(num_range[0], num_range[1])

        res = eval(str(num1) + " " + op + " " + str(num2))

        return "x " + op + " " + str(num2) + " = " + str(res), num1,"1"

    def random_quiz(self):
        pick=random.choice(list(capitals.keys()))
        correct_answer=capitals.get(pick)
        return pick,correct_answer,"2"

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = False
    server_thread.start()

    while True:
        try:
            time.sleep(1)
        except:
            break

    server.shutdown()
    server.server_close()

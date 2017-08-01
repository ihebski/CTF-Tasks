import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1',11222))
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

def search(l):
    for k in capitals.keys():
        if k == l:
            return capitals.get(k)
    return "false"

data = s.recv(2048)
print data

data = s.recv(2048)
question = data.split(' ')
ques = data.split(": ",1)[1]
ques = ques.rstrip('\r\n')
re = search(ques)
print question

if re != "false":
    correct_answer=re
    s.send(correct_answer + "\n")
elif question[3] == "-":
    s.send(str(int(question[4]) + int(question[6])) + "\n")
elif question[3] == "+":
    s.send(str(int(question[6]) - int(question[4])) + "\n")
elif question[3] == "*":
    s.send(str(int(question[6]) / int(question[4])) + "\n")
elif question[3] == "/":
    s.send(str(int(question[6]) * int(question[4])) + "\n")

for x in range(0, 500):
    data = s.recv(19)
    if data == "":
        exit(0)
    print data
    data = s.recv(512)
    question = data.split(' ')
    print question
    if ":" not in data:
        exit(''.join(question))
    ques = data.split(": ",1)[1]
    ques = ques.rstrip('\r\n')
    re = search(ques)
    if re != "false":
        correct_answer=re
        print "solution : ",correct_answer
        s.send(correct_answer + "\n")
    elif question[3] == "-":
        print "solution : ",str(int(question[4]) + int(question[6])) 
        s.send(str(int(question[4]) + int(question[6])) + "\n")
    elif question[3] == "+":
        print "solution : ",str(int(question[6]) - int(question[4]))
        s.send(str(int(question[6]) - int(question[4])) + "\n")
    elif question[3] == "*":
        print "solution : ",str(int(question[6]) / int(question[4]))
        s.send(str(int(question[6]) / int(question[4])) + "\n")
    elif question[3] == "/":
        print "solution : ",str(int(question[6]) * int(question[4]))
        s.send(str(int(question[6]) * int(question[4])) + "\n")

data = s.recv(2048)
print data

#s.send(str(20) + "\n")

s.close()

'''
crime attack task solution
flag : Bugs_Bunny{rOoTisEaSy001}

'''

#!/usr/bin/python
import requests, string
url = "http://127.0.0.1:5050/"
user = "flag:"
suffix1 = "BCDEFGHIJKL"
s = requests.Session()
baseline = []
while True:
    for i in range(50):
        r = s.get(url, params={'user':user+"#"+suffix1})
        auth = r.cookies['auth']
        baseline.append(len(auth))
        before = len(user)
        for c in string.printable:
            userfield = user+c+suffix1
            r = s.get(url, params={'user':userfield})
            auth = r.cookies['auth']
            if len(auth) < baseline[i]:
                user += c
                print user
                break
        if len(user) == before:
            print "[*] Flag: Bugs_Bunny{"+user.replace('flag:','')+"}"
            quit()

import math

import gmpy2
from Crypto.PublicKey import RSA


p = 2165121523231
q = 9456131321351327
e = 17
n = p * q
print "N: "+str(n) 
flag = "Bugs_Bunny{Baby_RSA_Its_Cool_Lik3_school_haHAha}"

d = lambda p, q, e: int(gmpy2.invert(e, (p-1)*(q-1)))
print ''
print d(p,q,e)
print ''
for i in flag:
    c = pow(ord(i),e,n)
    print c

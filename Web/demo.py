def C03011(Qml5):
	C12d =0
	for Po4M in Qml5:
		C12d =(31*C12d+ord(Po4M))& 0xFFFFFFFF
	return ((C12d + 0x80000000)& 0xFFFFFFFF) - 0X80000000
if __name__ == '__main__':

	user = raw_input('username: ')
	passwd = raw_input('password: ')
	if user != passwd :
		if C03011(passwd) == 2112 and C03011(user) == 2112:
			print ' this your flag'
			print "send me your solution when you solve it"
		else:
			print 'sorry try again'
	else:
		print 'sorry try again'
	




	

def changeB(long num,int base): #takes a number in base 10 and returns a number in any base 
	store = '0123456789ABCDEF'
	if num < base:
		return store[num]
	else:
		return changeB(num // base, base) + store[num % base]

def base2(unsigned long num,int base):
	return long(changeB(num,base))
	
def isPali(long num):
	if num == long(str(num)[::-1]):
		return True
	return False

def mainC(long limit):
	cdef long tot = 0
	for i in xrange(1, limit):
		if isPali(i) and isPali(base2(i, 2)):
			print i
			tot += i
	return tot


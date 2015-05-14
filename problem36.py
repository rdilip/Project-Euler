def changeB(num,base): #takes a number in base 10 and returns a number in base 2
	store = '0123456789ABCDEF'
	if num < base:
		return store[num]
	else:
		return changeB(num // base, base) + store[num % base]

def base2(num,base):
	return int(changeB(num,base))
	
def isPali(num):
	if int(num) == int(str(num)[::-1]):
		return True
	return False

def main(limit):
	tot = 0
	for i in xrange(1, limit):
		if isPali(i) and isPali(base2(i, 2)):
			tot += i
	return tot


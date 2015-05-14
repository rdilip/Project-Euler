def isprime(num):
	for i in xrange(2,int(num**0.5 + 1)):
		if num % i == 0:
			return False
	return True
tot = 0
for i in xrange(3,2000001,2):
	if isprime(i):
		tot += i
print tot + 2

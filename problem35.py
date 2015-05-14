def isPrime(num):
	if num == 1:
		return False
	for i in xrange(2,int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True

def numLen(num):
	return len(str(num))

def circular(num):
	if not isPrime(num):return False
	temp = (num % 10) * (10**(numLen(num) - 1)) + (num - (num % 10)) / 10
	while temp != num:
		if isPrime(temp):pass
		else:return False
		temp = (temp % 10) * (10**(numLen(temp) - 1)) + (temp - (temp % 10)) / 10
	return True

def numCircPrime(limit):
	count = 0
	for i in xrange(1,limit+1):
		if circular(i):
			count += 1
	return count
import time
start = time.time()
result = numCircPrime(1000000)
end = time.time()

print "The answer is %d, and it took %f seconds" % (result, end-start)

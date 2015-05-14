def isPrime(num):
	if num == 1:
		return False
	for i in xrange(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True
def l2r(num):
	dig = len(str(num))
	for i in xrange(1,dig + 1):
		if isPrime(num % 10**i) == False:
			return False
			break
	return True

def r2l(num):
	res = []
	temp = num
	while temp >= 1:
		res.append(temp)
		temp = (temp - (temp % 10)) / 10
	if any(isPrime(x) == False for x in res):
		return False
	return True

def mark(sieve, x):
	for i in xrange(x + x, len(sieve), x):
		sieve[i] = False

def primeS(limit):
	M = [True] * limit
	for i in xrange(2, int(len(M) ** 0.5) + 1):
		if M[i]:
			mark(M, i)
	return M

def main(limit):
	Z = primeS(limit)
	tot = 0
	for i in xrange(10, len(Z)):
		if Z[i] and r2l(i) and l2r(i):
			tot += i
	return tot

import time
start = time.time()
result = main(1000000)
elapsed = time.time() - start

print "result %d found in %f seconds" % (result, elapsed)

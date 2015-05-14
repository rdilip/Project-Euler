import time
def fib():
	temp,res = 1,2
	while True:
		yield temp
		temp,res = res,res + temp
def PEproblem1(limit):
	x = fib()
	y = x.next()
	result = 0
	while y < limit:
		if y % 2 == 0:
			result += y
		y = x.next()
	return(result)
start = time.time()
for i in xrange(0,100000):result = PEproblem1(4000000)
elapsed = time.time() - start
print "result %s returned after %s seconds" % (result,elapsed)

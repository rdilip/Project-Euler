import time
start = time.time()
def factorial(n):
	num = 1
	for i in xrange(1,n+1):num=num * i
	return num
print factorial(40) / (factorial(20) * factorial(20))
end = time.time()
print end - start

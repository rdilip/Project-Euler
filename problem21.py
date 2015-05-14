import time
start = time.time()
def divisors(num):
	result = []
	for i in xrange(1, int(num**0.5) + 1):
		 if num % i == 0: result.extend([i,num / i])
	return result
def propSum(num):
	result = [i for i in divisors(num)]
	result.remove(num)
	return sum(result)
sieve = [True] * 10000
tot = 0
for i in xrange(2,10001):
	if i == propSum(propSum(i)) and propSum(i) != i:
		tot+=i
		print i
print tot	
end = time.time()
print end - start

import time
def divisors(num):
	result = []
	for i in xrange(1,int(num**0.5) + 1):
		if num % i == 0:result.extend((i, num / i))
	return result

start = time.time()
counter = 1
while counter:
	if len(divisors(counter * (counter + 1) / 2)) > 500:break
	counter += 1
elapsed = time.time() - start
print (counter * (counter + 1)) / 2
print(elapsed)

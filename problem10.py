import time
start = time.time()
sieve = [True] * 2000000

def mark(sieve, x):
	for i in xrange(x+x, len(sieve), x):
		sieve[i] = False

for i in xrange(2, int(len(sieve) ** 0.5) + 1):
	if sieve[i]:mark(sieve,i)

print sum(i for i in xrange(2,len(sieve)) if sieve[i])
end = time.time()
print end - start

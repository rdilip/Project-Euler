import time
def cyclen(d):
	count = 0
	num = 1.0 / float(d)
	used = set([])
	while True:
		num = num*10
		if int(num) not in used:
			count += 1	
			used.add(int(num))	
		else:break	
		num = float(str(num)[1::])
	return count
def longest_cycle(n):
	longest = 0
	long_d = 0
	for i in xrange(1,n):
		if cyclen(i) > longest:
			longest = cyclen(i)
			long_d = i
	return long_d
start = time.time()
print cyclen(6)
print cyclen(7)
res = longest_cycle(1000)
end = time.time()
print "The result is %f, and it took %f seconds" % (res, end-start)

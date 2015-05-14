import time;
start = time.time()
total = 0
for i in xrange(1, 1000):
	if i % 3 == 0:
		total = total + i
	elif i % 5 == 0 and i%3 != 0:
		total = total + i
print total
elapsed = time.time() - start
print "took %f seconds" % (elapsed)

def isPal(num):
	if num == int(str(num)[::-1]):
		return True
	return False
largest_pal = 0
for a in xrange(100,1000):
	for b in xrange(100,1000):
		if isPal(a*b):
			if (a*b) > largest_pal:
				largest_pal = a*b
print largest_pal
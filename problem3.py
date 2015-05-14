def is_prime(x):
    for i in xrange(2, int(x**0.5 + 1)):
	if x % i == 0:
		return False
	return True
print is_prime(143)
num = int(raw_input("What number?")

pf_large = 0

for i in xrange(2, int(num/2)):
	if is_prime(i):
		if num % i == 0:
			pf_large = i
return pf_large

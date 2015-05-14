def gcd(a, b):	
	while b != 0:
		(a, b) = (b, a%b)
	return a 
def lcm(a,b):
	return a * b / (gcd(a,b))
def lcmm(*args):
	return reduce(lcm, args)
my_list = []
for i in xrange(1,21):
	my_list.append(i)
print lcmm(*my_list)

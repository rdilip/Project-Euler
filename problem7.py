def isprime(n):
	for i in xrange(2,int(n**0.5)+1):	
		if n % i == 0:
			return False 
	return True 
count = 0
num = 2 

while count < 10001:
	if isprime(num):
		count += 1
	num += 1

print num - 1

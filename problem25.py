import time;
def fib():
	temp,num = 0,1
	while True:
		yield num
		temp,num=num,temp+num
start = time.time()
x = fib()
counter = 1
y = x.next()
while len(str(y)) < 5:
	y = x.next()
	counter += 1
elapsed = time.time() - start
print counter
print elapsed

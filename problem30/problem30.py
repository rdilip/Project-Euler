from problem30C import sum_digit_power
import time
start = time.time()
res = sum_digit_power(355000)
elapsed = time.time() - start
print "The result is %f, and it was found in %f seconds" % (res, elapsed)

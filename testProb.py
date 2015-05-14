from problem28 import main
from problem28C import mainC
import time
start = time.time()
result = main(1001)
elapsed = time.time() - start

print "Python: result %d found in %f seconds" % (result, elapsed)

start1 = time.time()
result1 = mainC(1001)
elapsed1 = time.time() - start1
print "Cython: result %d found in %f seconds" % (result1, elapsed1)



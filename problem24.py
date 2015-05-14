import itertools
num = [i for i in xrange(0,10)]
num.sort(key=str)
num = list(itertools.permutations(num))
newNum = [str(i) for i in num[999999]]
print "".join(newNum)

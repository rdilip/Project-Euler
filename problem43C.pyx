# coding: utf-8
from itertools import permutations
from itertools import ifilter
from math import factorial

def subProp(num):
    primes = [2,3,5,7,11,13,17]
    count = 0
    for i in xrange(2,9):
        if int(num[i - 1 : i + 2]) % primes[count] == 0:
            pass
        else:
            return False
            break
        count += 1
    return True

def mainC():
    res = []
    base = '1234567890'
    panDig = [''.join(i) for i in permutations(base)][factorial(8):]
    panDig = filter(lambda x:x[5] == '5' and int(x[3]) % 2 == 0, panDig)
    for perm in panDig:
        if subProp(perm) == 1:
            res.append(int(perm))
    return sum(res)

from libc.math cimport sqrt
def isPrime(int num):
    if num == 1:
        return False
    for i in xrange(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def permute(inp):
    res = []
    if len(inp) == 1: 
        res = [inp]
    for i, c in enumerate(inp):
        for perm in permute(inp[:i] + inp[i+1:]):
            res.append(c + perm)
    return res
def mainC():
    M = [int(i) for i in permute('1234567')]
    return max(filter(isPrime, M))

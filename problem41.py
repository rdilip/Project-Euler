# coding: utf-8
def mark(sieve, x):
    for i in xrange(x + x, len(sieve), x):
        sieve[i] = False
def primeSieve(limit):
    M = [True] * limit
    for i in xrange(2, int(limit ** 0.5) + 1):
        if M[i]:
            mark(M, i)
    return [i for i in xrange(2, limit) if M[i]]
def sieveLim(low, up):
    l1, l2 = primeSieve(low), primeSieve(up)
    return [i for i in l2 if i not in l1]

def isPrime(num):
    if num == 1:
        return False
    for i in xrange(2, int(num**0.5) + 1):
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
def main():
    M = [int(i) for i in permute('1234567')]
    return max(filter(isPrime, M))

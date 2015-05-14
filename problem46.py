# coding: utf-8
def primeGen():
    q = 2
    D = {}
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1
def isPrime(x):
    if x == 1:
        return False
    for i in xrange(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def oddComp():
    q = 9
    while True:
        if not isPrime(q):
            yield(q)
        q += 2
def squares():
    start = 1
    while True:
        yield start * start
        start += 1
        
def main():
    a = oddComp()
    x = a.next()
    b = squares()
    y = b.next()
    squareList = []
    while True:
        while y * 2 < x:
            squareList.append(y * 2)
            y = b.next()
        if any(isPrime(x - i) for i in squareList):
            pass
        else:
            return x
            break
        x = a.next()

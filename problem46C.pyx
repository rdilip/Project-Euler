cpdef isPrime(int x):
    if x == 1:
        return False
    for i in xrange(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def oddComp():
    cdef int q = 9
    while True:
        if not isPrime(q):
            yield(q)
        q += 2
def squares():
    cdef int start = 1
    while True:
        yield start * start
        start += 1
        
def mainC():
    a = oddComp()
    cdef int x = a.next()
    b = squares()
    cdef int y = b.next()
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

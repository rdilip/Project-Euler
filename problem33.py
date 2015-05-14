# coding: utf-8

import fractions
def main():
    p = fractions.Fraction(1,1)                
    for a in xrange(10,100):
        for b in xrange(a + 1, 100):
            if b % 10 == 0 or a == b:
                continue
            La, Lb = [a/10, a%10], [b/10, b%10]
            if any(i in Lb for i in La) and not all(i in Lb for i in La):
                if La[0] in Lb:
                    x = La[0]
                else:
                    x = La[1]
                La.remove(x)
                Lb.remove(x)
                if a * Lb[0] == b * La[0]:
                    p *= fractions.Fraction(La[0], Lb[0])
    return p

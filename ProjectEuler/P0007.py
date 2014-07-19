#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tadvent
#
# Created:     11/01/2013
# Copyright:   (c) tadvent 2013
# Licence:     GPLv3
#-------------------------------------------------------------------------------

from math import sqrt

#######################################
def primeGen(p = [2,3,5,7]):
    def nthPrime(n):
        assert(n > 0)
        t = p[-1]
        while len(p) < n:
            t += 2
            u = int(sqrt(t))
            for d in p:
                if d > u:
                    p.append(t)
                    break
                if t % d == 0:
                    break
        return p[n-1]
    return nthPrime

#######################################
def main():
    g = primeGen()
    print(g(10001))

if __name__ == '__main__':
    main()

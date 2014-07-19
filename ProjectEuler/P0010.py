'''
from math import sqrt

def primeGen(n):
    primes = [2, 3, 5, 7]
    for e in primes:
        yield e

    num = 7
    while num + 2 < n: # find next prime
        num += 2
        limit = int(sqrt(num) + 0.5)
        for e in primes:
            if e > limit:
                primes.append(num)
                yield num
                break
            elif num % e == 0:
                break

if __name__ == "__main__":
    print(sum(primeGen(2000000)))
#'''

##-------------------------------------
'''
max = 2000000

n = [1] * max
c = 2
t = 0

while c<max:
        t += c
        i = c
        while i < max:
                n[i] = 0
                i += c
        while c<max and n[c] == 0:
                c += 1

print(t)
#'''

###############################################
# another solution

from math import sqrt

def primes(n = 10):
    l = list(range(2, n))
    lim = int(sqrt(n + 1))
    r = []
    while(l[0] <= lim):
        r.append(l[0])
        l = [i for i in l if (i % l[0] != 0)]
    r.extend(l)
    return r

print(sum(primes(2000000)))

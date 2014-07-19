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
def maxPrime(n):
    d = 2
    while d < n:
        if n%d == 0:
            n //= d
        else:
            d += 1
    return n

def main():
    print(maxPrime(600851475143))

if __name__ == '__main__':
    main()

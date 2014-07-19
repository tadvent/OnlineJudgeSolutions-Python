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
def gcd(m,n):
    while n != 0:
        m,n = n,m%n
    return m

def lcm(m,n):
    return m*n//gcd(m,n)

def calc(n):
    l = 1
    for i in range(2,n+1):
        l = lcm(l,i)
    return l

def main():
    print(calc(20))

if __name__ == '__main__':
    main()

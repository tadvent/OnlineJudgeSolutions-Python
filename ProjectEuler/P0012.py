#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tadvent
#
# Created:     14/04/2013
# Copyright:   (c) tadvent 2013
# Licence:     GPLv3
#-------------------------------------------------------------------------------
from math import sqrt

def fac_count(num):
    upper = int(sqrt(num) + 1e-7)
    ret = 0
    for x in range(1, upper+1):
        if num % x == 0:
            ret += 2
    if num == upper * upper:
        ret -= 1
    return ret

def tri_gen():
    ret = 0
    num = 1
    while True:
        ret += num
        yield ret
        num += 1

def main():
    for i in tri_gen():
        if(fac_count(i) > 500):
            print(i)
            break

if __name__ == '__main__':
    main()  # about 10 secs

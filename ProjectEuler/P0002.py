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
def calc(ulimit):
    a,b = 1,1
    while b<=ulimit:
        yield b
        a,b = b,a+b

def main():
    print(sum(i for i in calc(4000000) if i%2==0))

if __name__ == '__main__':
    main()

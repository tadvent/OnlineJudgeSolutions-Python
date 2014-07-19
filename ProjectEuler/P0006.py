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
def calc(n):
    s = sum(i for i in range(n+1))
    ss = sum(i*i for i in range(n+1))
    return s*s - ss

def main():
    print(calc(100))

if __name__ == '__main__':
    main()

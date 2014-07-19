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
def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

def calc():
    curMax = 0
    curI = 0
    curJ = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            p = i*j
            if p<=curMax:
                break
            if isPalindrome(p):
                curMax, curI, curJ = p, i, j
    return curMax, curI, curJ

def main():
    m, i, j = calc()
    print(m, i, j)

if __name__ == '__main__':
    main()

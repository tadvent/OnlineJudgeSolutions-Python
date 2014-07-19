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
def judge(n):
    return(n % 3 == 0) or (n % 5 == 0)

def main():
    print(sum(i for i in range(1000) if judge(i)))

if __name__ == '__main__':
    main()

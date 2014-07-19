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

def collatz():
    ret = (1, 1)    # max num, col
    col_cnt = [0, 1]
    for n in range(2, 1000000):
        cnt = 0
        nc = n
        while(nc >= n):
            cnt += 1
            if nc % 2 == 0:
                nc //= 2
            else:
                nc = 3*nc + 1
        cnt += col_cnt[nc]
        col_cnt.append(cnt)
        if cnt > ret[1]:
            ret = (n, cnt)
    return ret

def main():
    print(collatz())

if __name__ == '__main__':
    main()

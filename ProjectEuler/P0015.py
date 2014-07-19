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

def latticePaths(n):
    cache = {(0,0): 1}
    def dfs(xy):
        if xy[0] < 0 or xy[1] < 0:
            return 0
        if xy in cache.keys():
            return cache[xy]
        ret = dfs((xy[0]-1, xy[1])) + dfs((xy[0], xy[1]-1))
        cache[xy] = ret
        return ret
    return dfs((n,n))

def main():
    print(latticePaths(20))

if __name__ == '__main__':
    main()

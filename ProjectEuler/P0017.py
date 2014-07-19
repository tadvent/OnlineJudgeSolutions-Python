#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tadvent
#
# Created:     25/04/2013
# Copyright:   (c) tadvent 2013
# Licence:     GPLv3
#-------------------------------------------------------------------------------

digits = ['zero', 'one', 'two', 'three', 'four', 'five',
'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
'eighteen', 'nineteen', 'twenty']
digits_n = [len(s) for s in digits]

tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
'sixty', 'seventy', 'eighty', 'ninety']
tens_n = [len(s) for s in tens]

def split_hundred(n):   # 1 <= n <= 999
    a = n // 100
    b = n % 100
    return a, b

def split_ten(n):   # 0 <= n <= 99
    a = n // 10
    b = n % 10
    return a, b

def num_n(n):   # 1 <= n <= 1000
    if(n == 1000):
        return 11   # 11 = len('onethousand')
    ret = 0
    a, b = split_hundred(n)
    if a > 0:
        ret += digits_n[a] + 7  # 7 = len('hundred')
        if b > 0:
            ret += 3    # 3 = len('and')
        else:   # b == 0
            return ret
    if b < 20:  # 0 < b < 20
        return ret + digits_n[b]
    c, d = split_ten(b)
    ret += tens_n[c]
    if d > 0:
        ret += digits_n[d]
    return ret


def main():
    print(sum(num_n(n) for n in range(1, 1001)))

if __name__ == '__main__':
    main()

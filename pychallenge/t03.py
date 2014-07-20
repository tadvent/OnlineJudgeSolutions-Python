import re

def dofind():
    filter = re.compile(r'(?<=[a-z][A-Z]{3})([a-z])(?=[A-Z]{3}[a-z])')
    allstr = open('t03.txt','r').read()
    print ''.join(filter.findall(allstr))

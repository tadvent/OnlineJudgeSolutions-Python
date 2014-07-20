import re

def dofilter():
    filter = re.compile(r'[^\@\!\#\$\%\^\&\*\(\)\_\+\[\]\{\}\n]')
    allstr = open('t02.txt','r').read()
    print "".join(filter.findall(allstr))
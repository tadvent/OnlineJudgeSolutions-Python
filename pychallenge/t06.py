import zipfile

zf = zipfile.ZipFile('t06.zip')

def findnext(nstr):
    text = zf.read(nstr+'.txt')
    start = text.find('Next nothing is ')+16
    if start<16: return text
    return text[start:]

def dofind(bgnum = '90052'):
    collect = []
    while True:
        collect.append(bgnum)
        bgnum = findnext(bgnum)
        if len(bgnum)>5:
            print bgnum
            break

    print ''.join((zf.getinfo(name+'.txt').comment for name in collect))

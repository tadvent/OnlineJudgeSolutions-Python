import urllib

urlbg=r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

def jug(text):
    start = text.find('and the next nothing is')+24
    if start<24 :
        return None
    return text[start:]

def dourl(ststr = '12345'):
    text = ''
    while(ststr):
        print ststr
        cul = urllib.urlopen(urlbg+ststr)
        text = cul.read()
        cul.close()
        ststr = jug(text)
    return text

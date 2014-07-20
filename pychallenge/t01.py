allstr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

def move(offset):
    def movech(ch):
        num = ord(ch)
        if num<97 or num>122: return ch
        num += offset
        if num>122: num-=26
        elif num<97: num+=26
        return chr(num)
    return movech

def chstr(offset,instr=allstr):
    return ''.join(map(move(offset),instr))

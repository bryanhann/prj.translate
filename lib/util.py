import string

def lmap(*a,**b): return list(map(*a,**b))
def isascii(ch): return (ch in string.ascii_letters)
def catenate( strS ): return ''.join(strS)

def lines_4_path(path):
    with open(path, 'r') as fd:
        return fd.readlines()

def text_4_path(path):
    with open(path, 'r') as fd:
        return fd.read()

__OLD_HACKERY="""
def braced(txt):
    return '{%s}' % txt

def dinsert(dic,key,val):
    if not key in dic:
        dic[key]=[]
    dic[key].append(val)
"""


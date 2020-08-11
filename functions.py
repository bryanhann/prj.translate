import string

def sections4lines(lines):
    acc=[[]]
    for line in lines:
        if line.startswith('<E>'):
            acc.append( [] )
        acc[-1].append(line)
    sections = [ ''.join(xx) for xx in acc ]
    return sections

def lines4fname(fname):
    with open(SRC) as fd:
        return fd.readlines()
def text4fname(fname):
    with open(SRC) as fd:
        return fd.read()
def braced(txt):
    return '{%s}' % txt

def blips4text(text):
    acc = [[]]
    for ch in text:
        if ch in string.ascii_letters:
            acc.append( [] )
        acc[-1].append(ch)
    return [ ''.join(xx) for xx in acc ]


SRC="./sample/passage.txt"
for section in sections4lines(lines4fname(SRC)):
    print section
#for section in sections:
#import sys

import string
import sys
DFILE="./sample/dictionary.txt"
BFILE="./sample/bad-dictionary.txt"
NULL=''
TAB='\t'

def parsefile(fname):
    with open(fname) as fd:
        lines=(line.strip() for line in fd.readlines())
    for ii,line in enumerate(lines):
        if not line: continue
        try:
            key,val=line.split('=')
        except ValueError:
            exit( 'ERROR on line %s' % ii )
        key=NULL.join( ch for ch in key if ch in string.ascii_letters ).lower().ljust(20)
        vals=TAB.join(val.split('|'))
        print(key, vals)
if __name__=='__main__':
    parsefile(sys.argv[1])

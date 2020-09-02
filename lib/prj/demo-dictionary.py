if __name__=='__main__':
    import string
    import sys
    NULL=''
    TAB='\t'
    fname = sys.argv[1]
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

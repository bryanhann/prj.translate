import sys
from wordbook.wbparser import wbDikt_errlist_4_wbPath

def wbparse():
    wbPath = sys.argv[1]
    wbDikt, errs = wbDikt_errlist_4_wbPath(wbPath)
    for item in wbDikt.items():
        sys.stdout.write(str(item) + '\n')
    for error in errs:
        sys.stderr.write(error + '\n')
    exit( 1 if errs else 0 )



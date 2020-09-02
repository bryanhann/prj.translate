import sys
from functions import *


if __name__ == '__main__':
    fname = sys.argv[1]
    text=text4fname(fname)
    blips=blips4text(text)
    for blip in blips:
        sys.stdout.write( braced(blip) )


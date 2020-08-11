import sys
from functions import *

SRC="./sample/passage.txt"

text=text4fname(SRC)
blips=blips4text(text)
for blip in blips:
    sys.stdout.write( braced(blip) )


import sys
from functions import *
from dev.functions import *
def test_func(datadir):
    passage_path = datadir["sample/passage.txt"]
    passage_text = text4fname(passage_path)
    assert passage_text.startswith('<E>')



def test_blips(datadir,regtest):
    blips=blips4fname( datadir["sample/passage.txt"] )
    regtest.write( repr(blips ) )

#if __name__ == '__main__':
#    fname = sys.argv[1]

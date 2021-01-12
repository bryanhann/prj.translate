from collections import OrderedDict
from local.util import slurplines, slurp

def _split2(text,sep1='$',sep2='|'):
    return [part.split(sep2) for part in text.split(sep1)]
def _enum2(seq_of_seq):
    for ii, seq in enumerate(seq_of_seq):
        for jj, item in enumerate(seq):
            yield ((ii,jj), item)

def map4path(path):
    return OrderedDict(_enum2(_split2(slurp(path))))


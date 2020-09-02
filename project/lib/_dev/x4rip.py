# naming scheme
# (assuming '$' and '|' are seperators)
#   rip : raw text if '$' separated strings, e.g. 'aa|bb$cc$dd|ee'
#   dip : raw text of '|' separated strings, e.g. 'aa|bb'
#   dipL : a list of dip
#   pipL : a list of pip
#   pipLL : a list of list of pip.

import pathlib
import collections

def enumerate_2D(LL):
    for ii_0, item_0 in enumerate(LL):
        for ii_1, item_1 in enumerate(item_0):
            yield ((ii_0,ii_1), item_1)


_DIP_SEP = '$'
_PIP_SEP = '|'

def dipL_4_rip(rip):  return rip.split(_DIP_SEP)
def pipL_4_dip(dip):  return dip.split(_PIP_SEP)
def pipLL_4_rip(rip): return list(map(pipL_4_dip, dipL_4_rip(rip)))
def pip2D_4_rip(rip): return collections.OrderedDict(enumerate_2D(pipLL_4_rip(rip)))

def mkfiles4ripT4base( ripT, base ):
    acc = []
    for (ii,jj),pipT in pip2D_4_rip(ripT).items():
        ii = str(ii).zfill(4)
        jj = str(jj).zfill(4)
        pipF = pathlib.Path(str(base) + '.%s.%s.tu' % (ii,jj))
        pipF.write_text(pipT)
        acc.append(pipF)
    return sorted(acc)


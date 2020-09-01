import pytest
import pathlib
import tempfile
from pprint import pprint
import constants as __CC

def slurp(path): return path.read_text(encoding=None)
def pjoin(list0): return __CC.SEP_P.join(list0)
def djoin(list0): return __CC.SEP_D.join(list0)

def nnnn(n):
    return str(n+10000)[-4:]

def IO_splitter_4_SrcDstSepExt(src, dst, sep, ext):
    def name4esn(ext,stem,n): return '%s.%s.%s' % (stem,n,ext)
    acc = []
    for nn, piece in enumerate( src.read_text(encoding=None).split(sep) ):
        current_name = name4esn(ext,src.stem,nnnn(nn))
        current_dst = (dst / name4esn(ext,src.stem,nnnn(nn)))
        current_dst.write_text(piece)
        acc.append(current_dst)
    return acc


def pipfiles_filtered_dipnum(pipfiles0, dipnum):
    def dipcode_4_pipfile(pipfile): return str(pipfile).split('.')[-3]
    pipfiles1 = sorted(list(pipfiles0))
    pipfiles2 = [ x for x in pipfiles1 if dipcode_4_pipfile(x) == nnnn(dipnum) ]
    return pipfiles2







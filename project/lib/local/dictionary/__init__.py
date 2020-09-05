import pathlib

from local.util import slurplines, isascii

def canonical(estring):
    return ''.join(filter(isascii,estring)).lower()

def eQL_4_dicFL(files):
    for path in map(pathlib.Path,files):
        for nn,line in enumerate(slurplines(path)):
            try:                lhs, rhs = line.split('=')
            except ValueError:  lhs, rhs = '', line
            yield (canonical(lhs), path.name, nn, rhs, line)

def cQL_4_eQL(eQL):
    for eng, fname, nn, chi_pipe, line in eQL:
        if not eng: continue
        for chi in chi_pipe.strip().split('|'):
            yield (chi, fname, nn, eng, line)


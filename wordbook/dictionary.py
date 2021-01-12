import pathlib

from transcheck.util import slurplines, isascii

def canonical(estring):
    return ''.join(filter(isascii,estring)).lower()

def eQG_4_dicFL(files):
    for path in map(pathlib.Path,files):
        for nn,line in enumerate(slurplines(path)):
            try:                lhs, rhs = line.split('=')
            except ValueError:  lhs, rhs = '', line
            yield (canonical(lhs), path.name, nn, rhs.strip(), line)

def cQG_4_eQS(eQS):
    for eng, fname, nn, chi_pipe, line in eQS:
        if not eng: continue
        for chi in chi_pipe.strip().split('|'):
            yield (chi, fname, nn, eng, line)

def eD_4_eQL(eQL):
    import collections
    def __fix(item):
        key, val = item
        return key, sorted(set(('|'.join(val)).split('|')))
    acc = collections.OrderedDict()
    for (e,dname,linenum,chis, line) in eQL:
        # reject bad e.
        if not e: continue
        key = e#Q[0]
        val = chis
        try: acc[key]
        except KeyError: acc[key]=[]
        acc[key].append(chis)
    return collections.OrderedDict(map(__fix,acc.items()))
def dictTuples_4_dictFiles(dictfiles):
    return sorted(eQG_4_dicFL(dictfiles))
dict_4_dictTuples = eD_4_eQL

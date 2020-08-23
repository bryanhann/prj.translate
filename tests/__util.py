from pprint import pformat
from dictionary import eng_one_4_files
def regtest__writers(regtest):
    def _write(ob): regtest.write(str(ob))
    def _writeline(ob): regtest.write(str(ob)+'\n')
    def _writelines(obS):
        for ob in obS:
            regtest.write(str(ob)+'\n')
    class Namespace: pass
    ret=Namespace
    ret.out = _write
    ret.line = _writeline
    ret.lines = _writelines
    return ret


def datadir__allfiles(datadir):
    return [
       datadir["sample/dictionary.txt"],
       datadir["sample/bad-dictionary.txt"],
    ]


def datadir__sample__eng_one(datadir):
    files = datadir__allfiles(datadir)
    eng_one = eng_one_4_files(files)
    return eng_one


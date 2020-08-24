#from pprint import pformat
def _regtest(regtest):
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



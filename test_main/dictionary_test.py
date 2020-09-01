#from __util import _regtest
import dictionary as UT # Under Test

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

def test__eGen1_4_dsfS(datadir, regtest):
    dsfS = [ datadir["sample/dictionary.txt"], datadir["sample/bad-dictionary.txt"], ]
    eGen1 = UT.eGen1_4_dsfS( dsfS )
    _regtest(regtest).lines(eGen1)

def test__cGen1_4_eGen1(datadir,regtest):
    dsfS = [ datadir["sample/dictionary.txt"], datadir["sample/bad-dictionary.txt"], ]
    eGen1 = UT.eGen1_4_dsfS(dsfS)
    cGen1 = UT.cGen1_4_eGen1(eGen1)
    _regtest(regtest).lines(cGen1)


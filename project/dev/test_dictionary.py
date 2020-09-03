import prj.dictionary as UT # Under Test

def textblock_4_seq(seq):
    return '\n'.join(map(str,list(seq)))

def test__eGen1_4_dsfS(datadir, regtest):
    dsfS = [ datadir["sample/dictionary.txt"], datadir["sample/bad-dictionary.txt"], ]
    eGen1 = UT.eGen1_4_dsfS( dsfS )
    regtest.write(textblock_4_seq(eGen1))

def test__cGen1_4_eGen1(datadir,regtest):
    dsfS = [ datadir["sample/dictionary.txt"], datadir["sample/bad-dictionary.txt"], ]
    eGen1 = UT.eGen1_4_dsfS(dsfS)
    cGen1 = UT.cGen1_4_eGen1(eGen1)
    regtest.write( textblock_4_seq(cGen1))


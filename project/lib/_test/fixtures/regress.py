import pytest
@pytest.fixture
def REGRESS(regtest):
    import _tools._formatter
    def textblock_4_seq(seq): return '\n'.join(map(str,list(seq)))
    class Namespace: pass
    X=Namespace()
    X.regtest = regtest
    X.blockwrite = lambda seq: regtest.write(textblock_4_seq(seq))
    X.formatter = _tools._formatter.Formatter( stdout=regtest )
    return X


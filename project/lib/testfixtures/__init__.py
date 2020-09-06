import pytest

class FB:
    # Fixture Bundle
    def __init__(self, *args):
        args = list(args)
        names = args.pop(-1).split()
        assert len(names)==len(args)
        for name,arg in zip(names,args):
            setattr(self, name, arg)


@pytest.fixture(scope='module')
def TEMP():
    import pathlib
    import tempfile
    return pathlib.Path(tempfile.mkdtemp())

@pytest.fixture
def THIS(regtest):
    from pprint import pprint
    def inner(item,show=False):
        if show: pprint(item)
        if not type(item)==type(''): item=repr(item)
        regtest.write(item)
    return inner

@pytest.fixture
def RIP(TEMP):
    import testdata
    class X: pass
    X.ripT = testdata.standard.ripfile.read_text(encoding=None)
    X.temp = TEMP
    return X


from testfixtures.dump import *
@pytest.fixture
def DUMP(dump,dumpfiles,ezrun): return FB( dump,dumpfiles,ezrun, 'dump dumpfiles ezrun'  )


from testfixtures.sample import *
@pytest.fixture
def SAMPLE(lines,text,rawcouplets,couplets): return FB( lines,text,rawcouplets,couplets, 'LINES TEXT RAWCOUPLETS COUPLETS')

from testfixtures.regress import REGRESS
#@pytest.fixture
#def REGRESS(regtest):
#    import _tools._formatter
#    def textblock_4_seq(seq): return '\n'.join(map(str,list(seq)))
#    class Namespace: pass
#    X=Namespace()
#    X.regtest = regtest
#    X.blockwrite = lambda seq: regtest.write(textblock_4_seq(seq))
#    X.formatter = _tools._formatter.Formatter( stdout=regtest )
#    return X


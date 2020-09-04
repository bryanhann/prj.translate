import pytest

class FB:
    # Fixture Bundle
    def __init__(self, *args):
        args = list(args)
        names = args.pop(-1).split()
        assert len(names)==len(args)
        for name,arg in zip(names,args):
            setattr(self, name, arg)


@pytest.fixture
def FORMAT(regtest):
    import _tools._formatter
    return _tools._formatter.Formatter( stdout=regtest )


@pytest.fixture(scope='module')
def TEMP():
    import pathlib
    import tempfile
    return pathlib.Path(tempfile.mkdtemp())


@pytest.fixture
def RIP(TEMP):
    import testdata
    class X: pass
    X.ripT = testdata.standard.ripfile.read_text(encoding=None)
    X.temp = TEMP
    return X


from _fixtures.dump import *
@pytest.fixture
def DUMP(dump,dumpfiles,ezrun): return FB( dump,dumpfiles,ezrun, 'dump dumpfiles ezrun'  )


from _fixtures.sample import *
@pytest.fixture
def SAMPLE(lines,text,rawcouplets,couplets): return FB( lines,text,rawcouplets,couplets, 'LINES TEXT RAWCOUPLETS COUPLETS')


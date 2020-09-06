import pytest
def _text(item):
    try: item = repr(iter(item) and list(item))
    except TypeError: item = repr(item)
    return '\n--------dump--------\n%s\n' % item

@pytest.fixture
def DUMP_dump(regtest):
    def inner(item): regtest.write( _text(item) )
    return inner

@pytest.fixture
def DUMP_dumpfiles(regtest):
    def pair4path(pth): return (pth, pth.read_text())
    def inner(paths): regtest.write(_text(list(map(pair4path,paths))))
    return inner

@pytest.fixture(scope='function')
def DUMP_ezrun(regtest):
    import local.ezrun
    return lambda cmd: regtest.write( local.ezrun.ezrun( cmd ))

#@pytest.fixture
#def x_dumpfiles(dump,regtest):
#    def inner(files):
#        zipped = zip(files, [x.read_text() for x in files])
#        return zipped
#        def inner2(item): regtest.write( _dump(item) )
#    return inner

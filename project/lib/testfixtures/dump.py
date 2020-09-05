import pytest

@pytest.fixture
def dump(regtest):
    def inner(item):
        try: item = repr(iter(item) and list(item))
        except TypeError: item = repr(item)
        regtest.write('\n--------dump--------\n%s\n' % item )
    return inner

@pytest.fixture
def dumpfiles(dump):
    return lambda files: dump( zip(files, [x.read_text() for x in files]) )

@pytest.fixture(scope='function')
def ezrun(regtest):
    import local.ezrun
    return lambda cmd: regtest.write( local.ezrun.ezrun( cmd ))


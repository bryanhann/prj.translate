import pytest

def __eager(item):
    try: return iter(item) and list(item)
    except TypeError: return item

@pytest.fixture
def x_dump(regtest):
    return lambda item: regtest.write('\n--------dump--------\n%s\n' % repr(__eager(item)) )

@pytest.fixture
def x_dumpfiles(x_dump):
    return lambda files: x_dump( zip(files, [x.read_text() for x in files]) )





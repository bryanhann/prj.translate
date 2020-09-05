import pytest

@pytest.fixture(scope='module')
def lines():
    from local.util import slurplines
    from testdata import sample
    return slurplines(sample.passage)

@pytest.fixture(scope='module')
def text():
    from testdata import sample
    return sample.passage.read_text()

@pytest.fixture(scope='module')
def rawcouplets(lines):
    import local.couplet as UT
    return UT.rawcouplets_4_lines(lines)

@pytest.fixture(scope='module')
def couplets(rawcouplets):
    import local.couplet as UT
    return list(map( UT.couplet_4_rawcouplet,rawcouplets))



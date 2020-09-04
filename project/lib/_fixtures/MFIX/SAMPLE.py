import pytest
import prj.couplet as UT
from prj.util import slurplines, slurp

from _here import sample

@pytest.fixture(scope='module')
def mfix_LINES(): return slurplines(sample.passage)

@pytest.fixture(scope='module')
def mfix_TEXT():  return sample.passage.read_text()

@pytest.fixture(scope='module')
def mfix_RAWCOUPLETS(mfix_LINES): return UT.rawcouplets_4_lines(mfix_LINES)

@pytest.fixture(scope='module')
def mfix_COUPLETS(mfix_RAWCOUPLETS): return list(map( UT.couplet_4_rawcouplet, mfix_RAWCOUPLETS))


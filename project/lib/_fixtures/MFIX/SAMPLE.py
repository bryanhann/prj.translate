import pytest
import prj.couplet as UT
from prj.util import slurplines, slurp

import _here

@pytest.fixture(scope='module')
def mfix_LINES(mfix_sample_passage): return slurplines(mfix_sample_passage)

@pytest.fixture(scope='module')
def mfix_TEXT(mfix_sample_passage):  return mfix_sample_passage.read_text()

@pytest.fixture(scope='module')
def mfix_RAWCOUPLETS(mfix_LINES): return UT.rawcouplets_4_lines(mfix_LINES)

@pytest.fixture(scope='module')
def mfix_COUPLETS(mfix_RAWCOUPLETS): return list(map( UT.couplet_4_rawcouplet, mfix_RAWCOUPLETS))

@pytest.fixture(scope='module')
def mfix_sample_passage():          return _here.DATADIR / 'sample/passage.txt'

@pytest.fixture(scope='module')
def mfix_sample_good_dictionary():  return _here.DATADIR / 'sample/dictionary.txt'

@pytest.fixture(scope='module')
def mfix_sample_bad_dictionary():   return _here.DATADIR / 'sample/bad-dictionary.txt'


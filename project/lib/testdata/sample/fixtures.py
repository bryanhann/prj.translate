import pytest
from local.util import slurplines
from testdata import sample
import local.couplet as UT

@pytest.fixture(scope='module')
def THESAMPLE_lines(): return slurplines(sample.passage)

@pytest.fixture(scope='module')
def THESAMPLE_text(): return sample.passage.read_text()

@pytest.fixture(scope='module')
def THESAMPLE_rawcouplets(THESAMPLE_lines): return UT.rawcouplets_4_lines(THESAMPLE_lines)

@pytest.fixture(scope='module')
def THESAMPLE_couplets(THESAMPLE_rawcouplets): return list(map( UT.couplet_4_rawcouplet,THESAMPLE_rawcouplets))



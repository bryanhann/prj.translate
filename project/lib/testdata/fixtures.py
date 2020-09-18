import pytest
import pytest
import collections

from local.util import slurplines
import local.couplet as __CC
import local.x4rip as __RIP
import local.dictionary as __DD
import local.blips as __BB
import testdata.standard as __STD

@pytest.fixture(scope='module')
def THESAMPLE_lines(): return slurplines(__STD . passage)

@pytest.fixture(scope='module')
def THESAMPLE_text(): return __STD.passage.read_text()

@pytest.fixture(scope='module')
def THESAMPLE_rawcouplets(THESAMPLE_lines): return __CC .rawcouplets_4_lines(THESAMPLE_lines)

@pytest.fixture(scope='module')
def THESAMPLE_couplets(THESAMPLE_rawcouplets): return list(map( __CC .couplet_4_rawcouplet,THESAMPLE_rawcouplets))

@pytest.fixture(scope='module')
def THE_pip2D(THE_rip):         return __RIP . pip2D_4_rip(THE_rip)

@pytest.fixture(scope='module')
def THE_rip():                  return __STD . english_ripfile .read_text()

@pytest.fixture(scope='module')
def THE_dictTuples():           return __DD . dictTuples_4_dictFiles( __STD . dictionaries)

@pytest.fixture(scope='module')
def THE_dikt(THE_dictTuples):   return __DD . dict_4_dictTuples(THE_dictTuples )

@pytest.fixture(scope='module')
def THE_plips(THE_pip2D):         return __BB . plips_4_pip(THE_pip2D[ (0,0) ])

@pytest.fixture(scope='module')
def CHI_rip():                  return __STD . chinese_ripfile.read_text()

@pytest.fixture(scope='module')
def CHI_pip2D(CHI_rip):         return __RIP .pip2D_4_rip(CHI_rip)

@pytest.fixture
def ENGCHI_pip2D(THE_pip2D, CHI_pip2D):
    SOURCE=THE_pip2D
    TRANS=CHI_pip2D
    assert SOURCE.keys() == TRANS.keys()
    acc = collections.OrderedDict()
    for key in SOURCE.keys():
        acc[key] = (SOURCE[key], TRANS[key])
    return acc
#---




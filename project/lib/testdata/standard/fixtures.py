import pytest
import collections
import testdata
import local.x4rip
import local.dictionary
import local.blips

@pytest.fixture(scope='module')
def THE_pip(THE_pip2D):         return THE_pip2D[(0,0)]
@pytest.fixture(scope='module')
def THE_pip2D(THE_rip):         return local.x4rip.pip2D_4_rip(THE_rip)
@pytest.fixture(scope='module')
def THE_rip():                  return testdata.standard.english_ripfile.read_text()
@pytest.fixture(scope='module')
def THE_dictTuples():           return local.dictionary.dictTuples_4_dictFiles( testdata.standard.dictionaries)
@pytest.fixture(scope='module')
def THE_dikt(THE_dictTuples):   return local.dictionary.dict_4_dictTuples(THE_dictTuples )
@pytest.fixture(scope='module')
def THE_plips(THE_pip):         return local.blips.plips_4_pip(THE_pip)

@pytest.fixture(scope='module')
def CHI_rip():                  return testdata.standard.chinese_ripfile.read_text()
@pytest.fixture(scope='module')
def CHI_pip2D(CHI_rip):         return local.x4rip.pip2D_4_rip(CHI_rip)



@pytest.fixture
def ENGCHI_pip2D(THE_pip2D, CHI_pip2D):
    SOURCE=THE_pip2D
    TRANS=CHI_pip2D
    assert SOURCE.keys() == TRANS.keys()
    acc = collections.OrderedDict()
    for key in SOURCE.keys():
        acc[key] = (SOURCE[key], TRANS[key])
    return acc


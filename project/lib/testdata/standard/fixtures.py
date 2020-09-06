import pytest

import testdata
import local.x4rip
import local.dictionary
import local.blips
@pytest.fixture(scope='module')
def THE_pip(THE_pip2D):         return THE_pip2D[(0,0)]
@pytest.fixture(scope='module')
def THE_pip2D(THE_rip):         return local.x4rip.pip2D_4_rip(THE_rip)
@pytest.fixture(scope='module')
def THE_rip():                  return testdata.standard.ripfile.read_text()
@pytest.fixture(scope='module')
def THE_dictTuples():           return local.dictionary.dictTuples_4_dictFiles( testdata.standard.dictionaries)
@pytest.fixture(scope='module')
def THE_dikt(THE_dictTuples):   return local.dictionary.dict_4_dictTuples(THE_dictTuples )

@pytest.fixture(scope='module')
def THE_plips(THE_pip):         return local.blips.plips_4_pip(THE_pip)

#from local.blips    import plips_4_pip
#from the_PIP        import pip

#plips = plips_4_pip(pip)





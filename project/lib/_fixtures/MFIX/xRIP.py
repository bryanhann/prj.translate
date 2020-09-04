import pytest
import _here

@pytest.fixture(scope='module')
def mfix_ripF():                    return _here.standard/ 'TheTitle.src'

@pytest.fixture(scope='module')
def mfix_ripT(mfix_ripF):           return mfix_ripF.read_text(encoding=None)

@pytest.fixture(scope='module')
def mfix_ripT(mfix_ripF):           return mfix_ripF.read_text(encoding=None)


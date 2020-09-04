import pytest
from _here import standard

@pytest.fixture(scope='module')
def mfix_ripT():           return standard.ripfile.read_text(encoding=None)



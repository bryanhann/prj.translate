from _tools import fixturehack as hack

import _fixtures.MFIX
from _fixtures.MFIX import *
exec(hack(_fixtures.MFIX, 'module'))
MFIX=xxFIX

import _fixtures.FFIX
from _fixtures.FFIX import *
exec(hack(_fixtures.FFIX))
FFIX=xxFIX

import pytest
@pytest.fixture
def FORMAT(regtest):
    import _tools._formatter
    return _tools._formatter.Formatter( stdout=regtest )


from _fixtures.MFIX.message import moo_the_module_test_message
from _fixtures.MFIX.message import moo_the_module_test_message as foobar_missive

import pytest
import pathlib
import tempfile
import _here

from _fixtures.MFIX.SAMPLE import *

@pytest.fixture(scope='module')
def mfix_ripF():                    return _here.DATADIR / 'TheTitle.src'

@pytest.fixture(scope='module')
def mfix_temp():                    return pathlib.Path(tempfile.mkdtemp())

@pytest.fixture(scope='module')
def mfix_ripT(mfix_ripF):           return mfix_ripF.read_text(encoding=None)

@pytest.fixture(scope='module')
def mfix_ripT(mfix_ripF):           return mfix_ripF.read_text(encoding=None)




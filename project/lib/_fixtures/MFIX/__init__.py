import pytest
import pathlib
import tempfile

@pytest.fixture(scope='module')
def mfix_temp(): return pathlib.Path(tempfile.mkdtemp())

from _fixtures.MFIX.SAMPLE import *
from _fixtures.MFIX.xRIP import *

from _fixtures.MFIX.message import moo_the_module_test_message
from _fixtures.MFIX.message import moo_the_module_test_message as foobar_missive







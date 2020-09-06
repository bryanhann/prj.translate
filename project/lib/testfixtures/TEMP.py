import pytest
import pathlib
import tempfile
@pytest.fixture(scope='module')
def TEMP(): return pathlib.Path(tempfile.mkdtemp())





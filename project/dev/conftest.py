from _conftest import *
import prj.util  as __U
import _tools._formatter as __F
import prj.couplet as __C
@pytest.fixture
def LINES(MFIX):
    return __U.lines_4_path(MFIX.sample_passage)

@pytest.fixture
def TEXT(MFIX):
    return __U.text_4_path(MFIX.sample_passage)

@pytest.fixture
def RAWCOUPLETS(LINES):
    return __C.rawcouplets_4_lines(LINES)

@pytest.fixture
def COUPLETS(RAWCOUPLETS):
    return map( __C.couplet_4_rawcouplet, RAWCOUPLETS)

@pytest.fixture
def FORMAT(regtest):
    return __F.Formatter( stdout=regtest )

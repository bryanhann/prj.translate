from _conftest import *

import prj.util  as __U
import _tools._formatter as __F
import prj.couplet as __C

PASSAGE_PATH = "sample/passage.txt"

@pytest.fixture
def LINES(datadir):
    return __U.lines_4_path(datadir[PASSAGE_PATH])

@pytest.fixture
def TEXT(datadir):
    return __U.text_4_path(datadir[PASSAGE_PATH])

@pytest.fixture
def RAWCOUPLETS(LINES):
    return __C.rawcouplets_4_lines(LINES)

@pytest.fixture
def COUPLETS(RAWCOUPLETS):
    return map( __C.couplet_4_rawcouplet, RAWCOUPLETS)

@pytest.fixture
def FORMAT(regtest):
    return __F.Formatter( stdout=regtest )

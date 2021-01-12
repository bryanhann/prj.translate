import pytest
from pathlib import Path

TESTS=Path(__file__).parent

@pytest.fixture
def MINI_WORDBOOK():
    return TESTS/'data/mini_wb.txt'

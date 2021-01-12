import subprocess
import pytest
import sys
from tools.ezrun import ezrun

def test_mini_workbook_regression(regtest,MINI_WORDBOOK):
    out = ezrun(['wbparse', MINI_WORDBOOK] )
    regtest.write(out)

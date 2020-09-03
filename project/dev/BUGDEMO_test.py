import pytest
import prj.dictionary as UT # Under Test
from pathlib import Path

def test_bug__lib_prj_dictionary__issue_handling_Path(datadir):
    path =  datadir["sample/dictionary.txt"]
    old = UT.eGen1_4_dsfS( [ path ] )
    new = UT.eGen1_4_dsfS( [ Path(path) ] )
    next(old) # ok
    next(new) # raises AttributeError




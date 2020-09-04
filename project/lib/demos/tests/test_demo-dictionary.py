from testdata import sample
from _fixtures import DUMP as D
TEMPLATE = 'python -m demos.demo-dictionary %s'
def test_bad_dict  (D): D.ezrun( TEMPLATE % sample.bad_dictionary   )
def test_good_dict (D): D.ezrun( TEMPLATE % sample.good_dictionary   )


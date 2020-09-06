from testdata import sample
from testfixtures.DUMP import DUMP_ezrun as EZRUN

TEMPLATE = 'python -m demos.demo-dictionary %s'

def test_bad_dict  (EZRUN): EZRUN( TEMPLATE % sample.bad_dictionary   )
def test_good_dict (EZRUN): EZRUN( TEMPLATE % sample.good_dictionary   )


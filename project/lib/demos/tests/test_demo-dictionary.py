from testdata.standard import bad_dictionary, good_dictionary
from testfixtures.DUMP import DUMP_ezrun as EZRUN

TEMPLATE = 'python -m demos.demo-dictionary %s'

def test_bad_dict  (EZRUN): EZRUN( TEMPLATE % bad_dictionary   )
def test_good_dict (EZRUN): EZRUN( TEMPLATE % good_dictionary   )


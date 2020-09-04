from prj.ezrun import ezrun
from _here import sample

TEMPLATE = 'python -m demos.demo-dictionary %s'

def test_bad_dict  (FFIX): FFIX.ezrun_with_capture( TEMPLATE % sample.bad_dictionary   )
def test_good_dict (FFIX): FFIX.ezrun_with_capture( TEMPLATE % sample.good_dictionary   )


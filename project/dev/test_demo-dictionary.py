from prj.ezrun import ezrun

TEMPLATE = 'python -m prj.demo-dictionary %s'

def test_bad_dict  (MFIX,FFIX): FFIX.ezrun_with_capture( TEMPLATE % MFIX.sample_bad_dictionary   )
def test_good_dict (MFIX,FFIX): FFIX.ezrun_with_capture( TEMPLATE % MFIX.sample_good_dictionary   )


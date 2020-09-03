from prj.ezrun import ezrun

TEMPLATE = 'python -m prj.demo-dictionary %s'

def test_bad_dict  (MFIX,regtest): regtest.write( ezrun( TEMPLATE % MFIX.sample_bad_dictionary   ))
def test_good_dict (MFIX,regtest): regtest.write( ezrun( TEMPLATE % MFIX.sample_good_dictionary  ))



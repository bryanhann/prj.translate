import local.dictionary as UT # Under Test
from testdata.standard import dictionaries as DICFL

def test_regress__eQL_4_dicFL (REGRESS): REGRESS.blockwrite( UT.eQG_4_dicFL ( DICFL                 ))
def test_regress__cQL_4_eQL   (REGRESS): REGRESS.blockwrite( UT.cQG_4_eQS   ( UT.eQG_4_dicFL(DICFL) ))


import prj.dictionary as UT # Under Test
import testdata

DICFL = testdata.sample.dictionaries

def test_regress__eQL_4_dicFL (REGRESS): REGRESS.blockwrite( UT.eQL_4_dicFL ( DICFL                 ))
def test_regress__cQL_4_eQL   (REGRESS): REGRESS.blockwrite( UT.cQL_4_eQL   ( UT.eQL_4_dicFL(DICFL) ))


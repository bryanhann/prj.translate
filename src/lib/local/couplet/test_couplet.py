from local.couplet import plips_4_couplets as FN
def test_regress_THESAMPLE_lines        (THIS, THESAMPLE_lines       ): THIS(THESAMPLE_lines,        show=0)
def test_regress_THESAMPLE_rawcouplets  (THIS, THESAMPLE_rawcouplets ): THIS(THESAMPLE_rawcouplets,  show=0)
def test_regress_THESAMPLE_couplets     (THIS, THESAMPLE_couplets    ): THIS(THESAMPLE_couplets,     show=0)
def test__plips                         (THIS, THESAMPLE_couplets    ): THIS(FN(THESAMPLE_couplets), show=0)

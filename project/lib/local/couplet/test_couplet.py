from local.couplet import plips_4_couplets as FN

def test_plips         (THESAMPLE_couplets,REGRESS): REGRESS.formatter.desc( 'the plips.')              .seq( FN(THESAMPLE_couplets) ).run()
def test_lines         (THESAMPLE_lines,REGRESS): REGRESS.formatter.desc( 'the lines.' )                .seq( THESAMPLE_lines         ).run()
def test_rawcouplets   (THESAMPLE_rawcouplets,REGRESS): REGRESS.formatter.desc( 'the raw couplets.' )   .seq( THESAMPLE_rawcouplets   ).run()
def test_couplets      (THESAMPLE_couplets,REGRESS): REGRESS.formatter.desc( 'the couplets.' )          .seq( THESAMPLE_couplets      ).run()



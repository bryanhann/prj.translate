from local.couplet import plips_4_couplets

def test_plips         (SAMPLE,REGRESS): REGRESS.formatter.desc( 'the plips.')         .seq( plips_4_couplets(SAMPLE.COUPLETS) ).run()
def test_lines         (SAMPLE,REGRESS): REGRESS.formatter.desc( 'the lines.' )        .seq( SAMPLE.LINES         ).run()
def test_rawcouplets   (SAMPLE,REGRESS): REGRESS.formatter.desc( 'the raw couplets.' ) .seq( SAMPLE.RAWCOUPLETS   ).run()
def test_couplets      (SAMPLE,REGRESS): REGRESS.formatter.desc( 'the couplets.' )     .seq( SAMPLE.COUPLETS      ).run()



from prj.couplet import plips_4_couplets

def test_plips         (SAMPLE,FORMAT): FORMAT.desc( 'the plips.')         .seq( plips_4_couplets(SAMPLE.COUPLETS) ).run()
def test_lines         (SAMPLE,FORMAT): FORMAT.desc( 'the lines.' )        .seq( SAMPLE.LINES         ).run()
def test_rawcouplets   (SAMPLE,FORMAT): FORMAT.desc( 'the raw couplets.' ) .seq( SAMPLE.RAWCOUPLETS   ).run()
def test_couplets      (SAMPLE,FORMAT): FORMAT.desc( 'the couplets.' )     .seq( SAMPLE.COUPLETS      ).run()



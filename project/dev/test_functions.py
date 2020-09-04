def plips_4_couplets(couplets):
    from prj.blips import plips_4_text
    return [plips_4_text(eng) for eng,chi in couplets]

def test_plips         (MFIX,FORMAT): FORMAT.desc( 'the plips.')         .seq( plips_4_couplets(MFIX.COUPLETS) ).run()
def test_lines         (MFIX,FORMAT): FORMAT.desc( 'the lines.' )        .seq( MFIX.LINES         ).run()
def test_rawcouplets   (MFIX,FORMAT): FORMAT.desc( 'the raw couplets.' ) .seq( MFIX.RAWCOUPLETS   ).run()
def test_couplets      (MFIX,FORMAT): FORMAT.desc( 'the couplets.' )     .seq( MFIX.COUPLETS      ).run()



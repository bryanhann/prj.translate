import prj.blips as __B

def test__the_sample_passage_startswith_ETAG(TEXT):
    assert TEXT.startswith('<E>')

def test__these_are_the_plips_from_the_sample_passage (COUPLETS,FORMAT):
    FORMAT \
    . desc('These are the plips from the passage.') \
    . seq( __B.plips_4_text(eng) for eng,chi in COUPLETS) \
    . run()

def test__these_are_the_lines_from_passage(LINES,FORMAT):
    FORMAT \
    . desc( 'These are the lines from the sample passage.' ) \
    . seq(LINES) \
    . run()

def test__these_are_the_raw_couplets_from_the_sample_passage(RAWCOUPLETS,FORMAT):
    FORMAT \
    . desc( 'These are the raw couplets from the sample passage' ) \
    . seq(RAWCOUPLETS) \
    . run()

def test__these_are_the_cooked_couplets_from_the_sample_passage(COUPLETS,FORMAT):
    FORMAT \
    . desc('These are the cooked couplets from the sample passage:') \
    . seq(COUPLETS) \
    . run()



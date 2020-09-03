import pytest
@pytest.fixture
def FORMAT(regtest):
    import _tools._formatter
    return _tools._formatter.Formatter( stdout=regtest )
def __plips(couplets):
    from prj.blips import plips_4_text
    return [plips_4_text(eng) for eng,chi in couplets]

def test_plips         (MFIX,FORMAT): FORMAT.desc( 'the plips.')         .seq( __plips(MFIX.COUPLETS) ).run()
def test_lines         (MFIX,FORMAT): FORMAT.desc( 'the lines.' )        .seq( MFIX.LINES         ).run()
def test_rawcouplets   (MFIX,FORMAT): FORMAT.desc( 'the raw couplets.' ) .seq( MFIX.RAWCOUPLETS   ).run()
def test_couplets      (MFIX,FORMAT): FORMAT.desc( 'the couplets.' )     .seq( MFIX.COUPLETS      ).run()



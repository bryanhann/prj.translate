

def test_X(MODFIX):
    pass


import stuff as __SS

def test_MODFIX_DIPSTRINGS  (regtest, MODFIX): regtest.write(repr(MODFIX.DIPSTRINGS ))
def test_MODFIX_DIPFILES    (regtest, MODFIX): regtest.write(repr(MODFIX.DIPFILES   ))
def test_MODFIX_PIPFILES    (regtest, MODFIX): regtest.write(repr(MODFIX.PIPFILES   ))
def test_MODFIX_TEMP        (regtest, MODFIX): regtest.write(repr(MODFIX.TEMP       ))

def test_B(MODFIX):
    assert MODFIX.DIPSTRINGS == list(map(__SS.slurp,MODFIX.DIPFILES))

def test_D(MODFIX):
    for dipnum,dipstring in enumerate(MODFIX.DIPSTRINGS):
        _pipfiles = __SS.pipfiles_filtered_dipnum( MODFIX.PIPFILES, dipnum )
        assert dipstring == __SS.pjoin(map(__SS.slurp,_pipfiles))


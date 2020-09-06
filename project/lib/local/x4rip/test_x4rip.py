from testfixtures.DUMP import DUMP_dump
import local.x4rip as UT # under test

def test_dipL_4_rip   (DUMP_dump,THE_rip): DUMP_dump( UT.dipL_4_rip  (THE_rip) )
def test_pipLL_4_rip  (DUMP_dump,THE_rip): DUMP_dump( UT.pipLL_4_rip (THE_rip) )
def test_pip2D_4_rip  (DUMP_dump,THE_rip): DUMP_dump( UT.pip2D_4_rip (THE_rip) )

from testfixtures.DUMP import DUMP_dumpfiles
def test_mkfiles4ripT4base___file_creation(TEMP,THE_rip):
    for name in ['apple', 'banana']:
        files = UT.mkfiles4ripT4base( THE_rip, TEMP/name)
        assert files == sorted(TEMP.glob(name + '.*'))

def test_mkfiles4ripT4base___regression(DUMP_dumpfiles, THE_rip, TEMP):
    DUMP_dumpfiles(UT.mkfiles4ripT4base( THE_rip, TEMP/'foo'))



import local.x4rip as UT # under test

SHORT_RIP = 'aa|bb$cc$dd|ee'
SHORT_DIPL = [ 'aa|bb', 'cc', 'dd|ee' ]
SHORT_PIPLL =[ ['aa','bb'], ['cc'], ['dd','ee'] ]
SHORT_ITEMS = [((0,0),'aa'),((0,1),'bb'),((1,0),'cc'),((2,0),'dd'),((2,1),'ee')]

def test_short_dipL_4_rip   (): assert SHORT_DIPL  == UT.dipL_4_rip   (SHORT_RIP)
def test_short_pipLL_4_rip  (): assert SHORT_PIPLL == UT.pipLL_4_rip  (SHORT_RIP)
def test_short_pip2D_4_rip  (): assert SHORT_ITEMS == list(UT.pip2D_4_rip(SHORT_RIP).items())



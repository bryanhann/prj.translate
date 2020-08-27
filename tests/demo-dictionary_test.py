from ezrun import ezrun

def test_bad_dict(datadir, regtest):
     cmd = 'python -m demo-dictionary %s' % datadir["sample/bad-dictionary.txt"]
     regtest.write( ezrun(cmd)  )

def test_good_dict(datadir, regtest):
     cmd = 'python -m demo-dictionary %s' % datadir["sample/dictionary.txt"]
     regtest.write( ezrun(cmd)  )


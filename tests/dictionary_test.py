import __util
from dictionary import eng_one_4_files
from dictionary import chi_one_4_eng_one

def test__eng_one_4_files(datadir, regtest):
    files = __util.datadir__allfiles(datadir)
    reg = __util.regtest__writers(regtest)

    eng_one = eng_one_4_files(files)
    eng_one = __util.datadir__sample__eng_one(datadir)
    reg.lines(eng_one)

def test__chi_one_4_eng_one(datadir,regtest):
    files = __util.datadir__allfiles(datadir)
    reg = __util.regtest__writers(regtest)
    eng_one = eng_one_4_files(files)
    #eng_one = __util.datadir__sample__eng_one(datadir)
    chi_one = chi_one_4_eng_one(eng_one)
    reg.lines(chi_one)


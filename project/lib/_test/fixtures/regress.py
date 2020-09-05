import pytest
import sys

class __SequenceDumper:
    def __init__(self, desc="undescribed", seq=[], cutoff=-1, stdout=sys.stdout,):
        self.desc(desc)
        self.seq(seq)
        self.cutoff(cutoff)
        self.stdout(stdout)
    def desc   (s,x): s._desc=x     ; return s
    def seq    (s,x): s._seq=x      ; return s
    def cutoff (s,x): s._cutoff=x   ; return s
    def stdout (s,x): s._stdout=x   ; return s
    def run(s):
        s._stdout.write( '\n' + s._desc + '\n' )
        for nn, item in enumerate(s._seq):
            nn = str(1000+nn)[-3:]
            line = nn + ' ' + repr(item) + '\n'
            s._stdout.write(line)

def __seq_dump(*a,**b):
    return __SequenceDumper( *a,**b )

@pytest.fixture
def REGRESS(regtest):
    class X: pass
    X.regtest       = regtest
    X.blockwrite    = lambda seq: regtest.write( '\n'.join(map(str,list(seq))))
    X.formatter     = __seq_dump( stdout=regtest )
    return X


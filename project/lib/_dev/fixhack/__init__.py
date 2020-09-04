import pytest

def _fn(): pass
_UNDER = '_'
_DUNDER='__'
_TYPE_FN = type(_fn)
_COMMA=','

_FIXTURE_ASSIGNMENT_TEMPLATE="""
    X.%s=%s
"""

_FIXTURE_MAIN_TEMPLATE="""
#import _here
import pytest
@pytest.fixture(scope="%s")
def xxFIX(%s):
    class NAMESPACE: pass
    X=NAMESPACE()
%s
    return X
"""


def __shortXlong_4_module(module):
    for _long in dir(module):
        _attr = getattr(module, _long)
        if _long.startswith(_DUNDER): continue
        if not type(_attr)==_TYPE_FN: continue
        if not _UNDER in _long: continue
        yield _long[_long.find(_UNDER)+1:], _long

def fixturehack(module, scope='function'):
    shortXlong = sorted(__shortXlong_4_module(module))
    arguments = _COMMA.join( xx[1] for xx in shortXlong )
    assignments = ''.join(  _FIXTURE_ASSIGNMENT_TEMPLATE % pair for pair in shortXlong  )
    return _FIXTURE_MAIN_TEMPLATE % (scope, arguments, assignments)

hack = fixturehack

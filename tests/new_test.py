import re

def pattern4dikt(dikt): 
    template = "(?P<%s>%s)"
    return '|'.join([ template % item for item in dikt.items() ])

def my_replace(m):
    for k,v in m.groupdict().items():
        if v:
            return '{%s|%s}' % (v,k)

def test_pattern_io():
    _dikt = {
        'GREECE' : "greece|greek|hellenic",
        'JOHN'   : "john|johannes",
    }
    _in = "I, john, aka johannes, am the greek man from the hellenic region."
    _out = "I, {john|JOHN}, aka {johannes|JOHN}, am the {greek|GREECE} man from the {hellenic|GREECE} region."
    _pattern=re.compile(pattern4dikt(_dikt))
    assert _out == _pattern.sub(my_replace, _in)

import pathlib

__standard  =pathlib.Path(__file__).parent/'standard'
__sample    =pathlib.Path(__file__).parent/'sample'

class standard: pass
standard.ripfile       = __standard / 'TheTitle.src'

class sample: pass
sample.passage          = __sample / 'passage.txt'
sample.good_dictionary  = __sample / 'dictionary.txt'
sample.bad_dictionary   = __sample / 'bad-dictionary.txt'
sample.dictionaries     = [sample.good_dictionary, sample.bad_dictionary]

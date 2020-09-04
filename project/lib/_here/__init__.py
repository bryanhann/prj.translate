import pathlib

__sample=pathlib.Path(__file__).parent/'sample'
__standard=pathlib.Path(__file__).parent/'standard'

standard = __standard

class sample: pass
sample.passage          = __sample / 'passage.txt'
sample.good_dictionary  = __sample / 'dictionary.txt'
sample.bad_dictionary   = __sample / 'bad-dictionary.txt'

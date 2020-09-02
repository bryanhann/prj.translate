from _here import fixturehack as hack

import _conftest.MFIX
from _conftest.MFIX import *
exec(hack(_conftest.MFIX, 'module'))
MFIX=xxFIX

import _conftest.FFIX
from _conftest.FFIX import *
exec(hack(_conftest.FFIX))
FFIX=xxFIX


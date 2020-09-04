from _tools import fixturehack as hack

import _fixtures.MFIX
from _fixtures.MFIX import *
exec(hack(_fixtures.MFIX, 'module'))
MFIX=xxFIX

import _fixtures.FFIX
from _fixtures.FFIX import *
exec(hack(_fixtures.FFIX))
FFIX=xxFIX


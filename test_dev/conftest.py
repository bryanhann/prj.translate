from pytest import fixture

@fixture(scope='module')
def __path():
    import __here__ as HERE
    return HERE.DATADIR / 'TheTitle.src'

@fixture(scope='module')
def __temp():
    import pathlib
    import tempfile
    return pathlib.Path(tempfile.mkdtemp())

@fixture(scope='module')
def __dollars(__path):
    return __path.read_text(encoding=None).split('$')

@fixture(scope='module')
def __dollarfiles( __temp , __path):
    import constants as CC
    import stuff as SS
    return SS.IO_splitter_4_SrcDstSepExt(__path,__temp,CC.SEP_D,CC.EXT_D)

@fixture(scope='module')
def __pipefiles( __temp , __dollarfiles):
    import constants as CC
    import stuff as SS
    acc = []
    for dollarfile in __dollarfiles:
        acc = acc + SS.IO_splitter_4_SrcDstSepExt( dollarfile, __temp , CC.SEP_P, CC.EXT_P)
    return acc

@fixture(scope='module')
def MODFIX(
    __temp,
    __path,
    __dollars,
    __dollarfiles,
    __pipefiles,
):
    class Namespace: pass
    xx = Namespace()
    xx.IO_TEMP          = __temp
    xx.PATH             = __path
    xx.DOLLARS          = __dollars
    xx.IO_DOLLAR_FILES  = __dollarfiles
    xx.IO_PIPE_FILES    = __pipefiles
    xx.PIPFILES    = __pipefiles
    xx.DIPSTRINGS  = __dollars
    xx.DIPFILES  = __dollarfiles
    xx.TEMP          = __temp
    return xx

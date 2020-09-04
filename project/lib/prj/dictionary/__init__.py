import pathlib
import prj.util as __U

DESC="""
    A [dsf] (dictionary source file) is a text file whose lines are of the form

        EngRaw + "=" + ChiPipe + "\n"

    where EngRaw is an English phrase and ChiPipe is a pipe-separated list
    of Chinese phrases.


    A list of [dsf]s is converted in to an [eGen1] (english generator 1) which
    generates 5-tuples headed by a canonical english phrase and containing
    debugging information.
"""


def canonical(estring):
    return ''.join(filter(__U.isascii,estring)).lower()

#-----------------------------------------------------------------------------
# Take a list of dsfS and yield 5-tuples each headed by a canonical english
# phrase and containing debugging information.

def eGen1_4_dsfS(dsfS):
    for dsf in dsfS:
        fname = pathlib.Path(dsf).name
        for nn,line in enumerate(__U.lines_4_path(dsf)):
            try:
                lhs, rhs = line.split('=')
            except ValueError:
                lhs, rhs = '', line
            yield (canonical(lhs), fname, nn, rhs, line)

#-----------------------------------------------------------------------------
# Take a list of dsfS and yield 5-tuples each headed by a canonical english
# phrase and containing debugging information.

def cGen1_4_eGen1(eng1):
    for eng, fname, nn, chi_pipe, line in eng1:
        if eng:
            chi_list = chi_pipe.strip().split('|')
            for chi in chi_list:
                yield (chi, fname, nn, eng, line)


import string
from pathlib import Path

#
# The translation aid is based on a *wordbook* -- essentially a dictionary whose source
# form is a plain text *wordbook file* whose entries are lines of the form
#
#         chrismation=堅振|傅膏|堅振傅膏|傅油=chrismation|chrismatory|chrismal|chrismated
#
# which is to say strings of the form '{key}={chinese}={english} where:
#         {key} is a canonical lowercase english term without spaces,
#         {chinese} is a pipe seperated list of chinese terms corresponding to {key}, and
#         {english} is a regular expression whose matches correspond to {key}.
#
# All functionality of this codebase depends on the wordbook. The source *wordbook file*
# is parsed my the function [wbDict_errlist_4_wbPath] which takes as it's sole argument
# a path (either string or Path object) to the source *wordbook file*. It promises to
# return a dictionary object *wordbook dictionary* and a list object *workbook errors*.
#
# The returned *workbook dictionary* object will have items that correspond to synactically
# correct lines. The correspondance is according to this form:
#         workbood file line:    "{key}|{chinese}|{english}"
#         workbook dict item:    ( "{key}" , [ "{chinese}" | "{english}" ] )
# Malformed lines will be skipped, as will lines with keys which have already been seen
# a previous line. For each skipped line, an error message will be appended to the
# *workbook errors* list.
#
# Variable names:
#
#    wbPath -- a path string or Path object pointing to a *wordbook file*
#    wbDikt -- a *workbook dictionary*
#


def _is_good_key(key):
    for ch in key:
        if not ch in string.ascii_letters + string.digits:
            return False
    if not key:
        return False
    return True


def wbDikt_errlist_4_wbPath(wbPath):
    """Do a best effort parsing of file [fname] while storing accumulated errors.
    eg: if src has the line
        chrismation=堅振|傅膏|堅振傅膏|傅油=chrismation|chrismatory|chrismal|chrismated
    then
        return_val['chrismation'] = ['堅振|傅膏|堅振傅膏|傅dd油', 'chrismation|chrismatory|chrismal|chrismated']
    """

    # expect wbPath is pathable
    wbPath = Path(wbPath)

    wbDikt = {}
    errlist = []
    for ii, line in enumerate( wbPath.read_text().split('\n') ):
        triple = line.split('=')
        if not len(triple)==3:
            errlist.append('line %s: malformed triple: %s' % (ii, triple))
        elif triple[0] in wbDikt:
            errlist.append('line %s: repeated key: %s' % (ii, triple))
        elif not _is_good_key(triple[0]):
            errlist.append('line %s: bad key: %s' % (ii, triple))
        else:
            wbDikt[ triple[0] ] = triple[1:]

    # sort the dikt before returning
    wbDikt = dict(sorted(wbDikt.items()))
    return wbDikt,errlist




from collections import OrderedDict
from collections import namedtuple


Entry=namedtuple('Entry', 'canonical chinese regular'.split() )
def _entry_4_line(line):
    return Entry(*[x.strip() for x in line.split('=')])
def _item_4_entry(entry):
    return entry.canonical, entry
def map4path(path):
    with open(path) as fd:
        return OrderedDict( map(_item_4_entry, map(_entry_4_line,fd)))



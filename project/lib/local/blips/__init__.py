import string
import local.util as __U

def plips_4_text(text):
    PIPE='|'
    assert not PIPE in text
    acc = []
    for ch in text:
        if __U.isascii(ch):
            acc.append(PIPE)
        acc.append(ch)
    return ''.join(acc)


__OLD_HACKERY="""
def plips_4_path(path):
    return plips_4_text(text_4_path(path))
"""


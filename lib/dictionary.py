#import string
#import sys
import functions as fn

#def isascii(ch):
#    return (ch in string.ascii_letters)

def norm4estring(estring):
    return ''.join(filter(fn.isascii,estring)).lower()

def eng_one_4_files(files):
    for fname in files:
        for nn,line in enumerate(fn.slurplines(fname)):
            try:
                lhs, rhs = line.split('=')
            except ValueError:
                lhs, rhs = '', line
            key = lhs and norm4estring(lhs)
            yield (key, fname.basename, nn, rhs, line)

def chi_one_4_eng_one(eng_one):
    for eng, fname, nn, chi_pipe, line in eng_one:
        if eng:
            chi_list = chi_pipe.strip().split('|')
            for chi in chi_list:
                yield (chi, fname, nn, eng, line)



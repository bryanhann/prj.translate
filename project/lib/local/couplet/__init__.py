from local.blips import plips_4_pip
def plips_4_couplets(couplets):
    return [plips_4_pip(eng) for eng,chi in couplets]

E_TAG='<E>'
C_TAG='<C>'
def rawcouplets_4_lines(lines):
    acc=[[]]
    for line in lines:
        if line.startswith('<E>'):
            acc.append( [] )
        acc[-1].append(line)
    rawcouplets = [ ''.join(xx) for xx in acc ]
    return rawcouplets

def couplet_4_rawcouplet(raw):
    assert type(raw) == type('')
    if not raw.startswith(E_TAG):
        return ('','')
    cut=raw.find(C_TAG)
    e_raw = raw[:cut]
    c_raw = raw[cut:]
    e_text = e_raw[ len(E_TAG): ]
    c_text = c_raw[ len(E_TAG): ]
    assert e_text.find(E_TAG) == -1
    assert c_text.find(C_TAG) == -1
    assert e_text.find(C_TAG) == -1
    assert c_text.find(E_TAG) == -1
    assert raw == E_TAG + e_text + C_TAG + c_text
    return (e_text, c_text)


from environ import env
import wordbook
import unit

DICT_MAP = wordbook.map4path(env.DICT_PATH)
ENG_MAP = unit.map4path(env.ENG_PATH)
CHI_MAP = unit.map4path(env.CHI_PATH)

def test_dikt(THIS): THIS(DICT_MAP)
def test_eng(THIS): THIS(ENG_MAP)
def test_chi(THIS): THIS(CHI_MAP)


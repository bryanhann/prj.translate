import pytest
from pprint import pprint

@pytest.fixture
def THIS(regtest):
    def inner(item,show=False):
        if show: pprint(item)
        if not type(item)==type(''): item=repr(item)
        regtest.write(item)
    return inner


import pytest

def test___MFIX_the_module_test_message__should_have_module_scope(MFIX):
    assert MFIX.the_module_test_message == 'I have module scope'
def test___MFIX_missive__should_have_module_scope(MFIX):
    assert MFIX.missive == 'I have module scope'

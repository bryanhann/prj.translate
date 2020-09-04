import pytest
@pytest.fixture(scope='module')
def moo_the_module_test_message(): return 'I have module scope'


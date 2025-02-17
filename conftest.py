import pytest


@pytest.fixture(scope="session")
def prework():
    print("i will do browser related setup before the testcase")
    return "pass"

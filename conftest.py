import pytest


@pytest.fixture(scope="session")
def prework():
    print("i will do browser related setup before the testcase")
    return "pass"

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

import pytest

# FIXTURE -scope at module level will only execute once for the entire test file. @pytest.fixture(scope="module")
# Function level- fixture will run everytime whenever it find the linkage. @pytest.fixture(scope="function")

#scope= "class" runs only once for a class
#scope= "session"


def test_initialchcek(prework):

    print("test has passed")

def test_anotherchcek(prework):
     print("another test ")


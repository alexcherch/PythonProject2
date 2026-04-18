import pytest


@pytest.fixture
def numbers():
    return "321"


@pytest.fixture
def letters():
    return "olleh"


@pytest.fixture
def my_list():
    return [1, 2, 3, 4, 5]

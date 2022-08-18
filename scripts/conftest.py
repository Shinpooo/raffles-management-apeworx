import pytest
from ape import accounts


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def receiver(accounts):
    return accounts[1]

@pytest.fixture
def raffle_participants(accounts):
    return accounts[1]
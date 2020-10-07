import pytest

from dining_philosophers.forks import Fork
from dining_philosophers.philosophers import Philosopher


@pytest.fixture
def fork():
    return Fork(0)


@pytest.fixture
def philosopher():
    left_fork = Fork(0)
    right_fork = Fork(1)

    return Philosopher(0, [left_fork, right_fork])

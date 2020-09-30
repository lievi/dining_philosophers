import pytest

from dining_philosophers.forks import Fork
from dining_philosophers.philosophers import Philosopher


@pytest.fixture
def fork():
    return _fork_factory()


@pytest.fixture
def philosopher():
    left_fork = _fork_factory()
    right_fork = _fork_factory()

    return Philosopher(0, [left_fork, right_fork])


def _fork_factory() -> Fork:
    return Fork()

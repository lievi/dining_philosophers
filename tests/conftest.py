import pytest
import mock

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


@pytest.fixture
def mock_sleep():
    with mock.patch('time.sleep', return_value=None) as mock_sleep:
        yield mock_sleep

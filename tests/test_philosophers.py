from dining_philosophers.forks import Fork
import pytest

from dining_philosophers.constants import ForkState, PhilosopherState
from dining_philosophers.exceptions import PhilosopherWithSameIdException
from dining_philosophers.philosophers import Philosopher
from dining_philosophers.forks import Fork


class TestPhilosophersInitialization:
    def test_create_philosopher(self):
        ID = 0

        philosopher = Philosopher(ID)

        assert philosopher.id == ID
        assert philosopher.state == PhilosopherState.THINKING

    # def test_assign_fork_to_a_philosopher_should_only_be_able_to_assign_two_forks(  # noqa
    #     self,
    # ):
    #     forks = (Fork() for _ in range(3))

    #     philosopher = Philosopher(0)

    #     for fork in forks:
    #         philosopher.fork = fork

    #     assert len(philosopher.fork) == 2

    def test_eat_as_owner_of_both_forks_should_set_state_to_eat(self):
        ...

    def test_eat_with_missing_ownership_of_forks_should_request_to_both_neighbors( # noqa
        self
    ):
        ...

    def test_think_should_set_state_to_thinking_and_set_the_fork_state_to_dirty( # noqa
        self
    ):
        ...

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

    # TODO: set this on the dining table class
    # def test_create_philosopher_with_same_id_should_raise(self):
    #     Philosopher(0)
    #     with pytest.raises(PhilosopherWithSameIdException):
    #         Philosopher(0)

    # TODO: set this on the dining table class
    # def test_assign_a_fork_to_a_philosopher_with_the_lowest_id_should_assing_a_fork(  # noqa
    #     self,
    # ):
    #     ...

    # TODO: set this on the dining table class
    # def test_assign_a_fork_to_a_philosopher_in_wich_its_neighbor_already_have_one_fork_should_not_assing(  # noqa
    #     self,
    # ):
    #     ...

    # def test_assign_fork_to_a_philosopher_should_only_be_able_to_assign_two_forks(  # noqa
    #     self,
    # ):
    #     forks = (Fork() for _ in range(3))

    #     philosopher = Philosopher(0)

    #     for fork in forks:
    #         philosopher.fork = fork

    #     assert len(philosopher.fork) == 2


class TestPhilosopherThinkingState:

    def test_philosopher_with_dirty_forks_receives_a_request_from_neighbor_should_clean_it_and_send_a_fork(  # noqa
        self,
    ):

        fork = Fork()

        philosopher = Philosopher(0)
        neighbor = Philosopher(1)

        # Both philosophers have the same fork in common, so they're neighbors
        philosopher.fork.append(fork)
        neighbor.fork.append(fork)

        # The current owner is a philosopher
        fork.current_owner = philosopher

        philosopher.receive_request(neighbor, fork)

        assert philosopher.state == PhilosopherState.THINKING
        assert fork.current_owner == neighbor
        assert fork.state == ForkState.CLEAN

    def test_verify_if_have_any_saved_requests_should_fulfill_the_requests(
        self,
    ):
        pass


class TestPhilosopherHungryState:
    def test_eat_with_both_forks_should_change_state_to_eating(self):
        ...

    def test_eat_with_no_fork_should_request_fork_to_both_neighbors(self):
        ...

    def test_eat_with_one_fork_should_request_fork_to_the_neighbor_that_have_a_fork(  # noqa
        self,
    ):
        ...

    def test_receive_request_from_some_neighbor_with_a_dirty_fork_should_clean_it_and_send(  # noqa
        self,
    ):
        ...

    def test_receive_request_from_some_neighbor_with_a_clean_fork_should_save_this_request_and_not_send(  # noqa
        self,
    ):
        ...

    def test_receive_a_fork_should_try_to_eat(self):
        ...


class TestPhilospherEatingState:
    def test_receive_request_while_eating_should_save_the_request(self):
        ...

    def test_philosopher_finish_eating_should_change_state_to_thinking(self):
        ...

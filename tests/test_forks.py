from dining_philosophers.constants import ForkState
from dining_philosophers.forks import Fork
from dining_philosophers.philosophers import Philosopher, PhilosopherState


class TestForks:
    def test_create_fork_should_initiate_with_the_dirty_state(self):
        current_owner = Philosopher(0)
        fork = Fork(current_owner)

        assert fork.state == ForkState.DIRTY

    def test_receive_request_with_same_owner_should_do_nothing(self):
        ...

    def test_receive_request_from_some_neighbor_with_dirty_state_should_clean_it_and_change_owner( # noqa
        self
    ):
        ...

    def test_receive_request_from_both_neighbors_should_lock_for_the_first_requester( # noqa
        self
    ):
        ...

    def test_receive_request_from_some_neighbor_with_clean_state_should_wait_until_the_owner_is_done( # noqa
        self
    ):
        ...


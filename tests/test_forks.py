import mock

from dining_philosophers.constants import ForkState
from dining_philosophers.forks import Fork
from dining_philosophers.philosophers import Philosopher


class TestForks:
    def test_create_fork_should_initiate_with_the_dirty_state(self):
        fork = Fork()

        assert fork.state == ForkState.DIRTY

    def test_receive_request_with_same_owner_should_do_nothing(
        self, fork: Fork, philosopher: Philosopher
    ):
        fork._owner = philosopher

        fork.request(philosopher)

        assert fork._owner == philosopher

    def test_receive_request_from_some_neighbor_with_dirty_state_should_clean_it_and_change_owner( # noqa
        self, fork: Fork, philosopher: Philosopher
    ):
        another_fork = Fork()
        another_philosopher = Philosopher(1, (fork, another_fork))

        fork._owner = another_philosopher

        fork.request(philosopher)

        assert fork.state == ForkState.CLEAN
        assert fork._owner == philosopher

    def test_receive_request_from_both_neighbors_should_lock_for_the_first_requester( # noqa
        self
    ):
        ...

    def test_receive_request_from_some_neighbor_with_clean_state_should_wait_until_the_owner_is_done( # noqa
        self, fork: Fork, philosopher: Philosopher
    ):
        another_fork = Fork()
        another_philosopher = Philosopher(1, (fork, another_fork))

        fork.state = ForkState.CLEAN
        fork._owner = another_philosopher

        with mock.patch(
            'dining_philosophers.forks.Condition.wait'
        ) as mock_wait:
            fork.request(philosopher)

            assert mock_wait.called

    def test_done_should_change_state_to_dirty_and_notify(
        self, fork: Fork, philosopher: Philosopher
    ):
        with mock.patch(
            'dining_philosophers.forks.Condition.notify_all'
        ) as mock_notify_all:
            fork.done()

            assert fork.state == ForkState.DIRTY
            assert mock_notify_all.called

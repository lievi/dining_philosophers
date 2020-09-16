from dining_philosophers.constants import ForkState
from dining_philosophers.forks import Fork
from dining_philosophers.philosophers import Philosopher, PhilosopherState


class TestForks:
    def test_create_fork_should_initiate_with_the_dirty_state(self):
        current_owner = Philosopher(0)
        fork = Fork(current_owner)

        assert fork.state == ForkState.DIRTY

    # def test_receive_a_

    # FIXME: i guess that this should be on the main tests
    def test_create_a_fork_for_every_pair_of_philosopher_on_the_table(self):
        ...

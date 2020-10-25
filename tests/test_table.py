import mock

from dining_philosophers.table import Table
from dining_philosophers.forks import Fork


class TestTable:
    def test_start_dining_should_start_the_philosophers_threads(self):
        table = Table()
        with mock.patch(
            'dining_philosophers.philosophers.threading.Thread.start'
        ) as mock_start_thread:
            table.start_dining()

        mock_start_thread.assert_called()
        mock_start_thread.call_count == table.PHILOSOPHERS_ON_TABLE

    def test_create_forks_should_create_a_fork_for_each_philosopher_on_table(self): # noqa
        number_of_philosophers = 5
        forks = Table._create_forks(number_of_philosophers)

        assert len(forks) == number_of_philosophers

        for id, fork in enumerate(forks):
            assert fork.id == id

    def test_create_philosophers_should_append_the_right_neighbors_forks(
        self
    ):
        number_of_philosophers = 5
        expected_neighbors = (
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 0)
        )

        forks = [Fork(i) for i in range(number_of_philosophers)]

        philosophers = Table._create_philosophers(
            number_of_philosophers, forks
        )

        for id, philosopher in enumerate(philosophers):
            fork_ids = tuple(fork.id for fork in philosopher.forks)

            assert fork_ids == expected_neighbors[id]

    def test_first_philosopher_should_be_owner_of_both_forks(self):
        number_of_philosophers = 2

        forks = [Fork(i) for i in range(number_of_philosophers)]

        philosophers = Table._create_philosophers(
            number_of_philosophers, forks
        )

        for fork in philosophers[0].forks:
            assert fork._owner == philosophers[0]

        for fork in philosophers[1].forks:
            assert fork._owner == philosophers[0]

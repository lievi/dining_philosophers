import logging

import mock

from dining_philosophers.constants import PhilosopherState
from dining_philosophers.philosophers import Philosopher
from dining_philosophers.forks import Fork


class TestPhilosophers:
    def test_create_philosopher(self):
        ID = 0

        left_fork = Fork(0)
        right_fork = Fork(1)

        philosopher = Philosopher(ID, (left_fork, right_fork))

        assert philosopher.id == ID
        assert philosopher.state == PhilosopherState.THINKING

    def test_run_philosopher_thread(self):
        ID = 0

        left_fork = Fork(0)
        right_fork = Fork(1)

        philosopher = Philosopher(ID, (left_fork, right_fork))

        philosopher.start()

    def test_run_philosopher_thread_with_philosopher_already_full_should_log_and_return( # noqa
        self, philosopher: Philosopher, caplog
    ):
        expected_log = f'{str(philosopher)} is full'
        philosopher.full = 3

        with caplog.at_level(logging.INFO):
            philosopher.run()

        caplog.records

        log_messages = [log.message for log in caplog.records]
        assert expected_log in log_messages

    def test_run_philosopher_thread_with_philosopher_should_eat_until_he_is_hungry( # noqa
        self, philosopher: Philosopher, caplog
    ):

        expected_log = f'{str(philosopher)} is full'

        with caplog.at_level(logging.INFO), mock.patch(
            'dining_philosophers.philosophers.Philosopher.eat'
        ), mock.patch(
            'dining_philosophers.philosophers.Philosopher.think'
        ):
            philosopher.run()

        caplog.records

        log_messages = [log.message for log in caplog.records]
        assert expected_log in log_messages

    def test_eat_as_owner_of_both_forks_should_set_state_to_eat(
        self, philosopher: Philosopher, mock_sleep
    ):
        assert philosopher.state == PhilosopherState.THINKING

        for fork in philosopher.forks:
            fork._owner = philosopher

        philosopher.eat()

        assert philosopher.state == PhilosopherState.EATING

    def test_eat_with_missing_ownership_of_forks_should_request_to_both_neighbors(  # noqa
        self, philosopher: Philosopher, mock_sleep
    ):
        with mock.patch("dining_philosophers.forks.Fork.request"):
            philosopher.eat()

            for fork in philosopher.forks:
                fork.request.assert_called_with(philosopher)

    def test_think_should_set_state_to_thinking_and_done_eating_with_the_forks(  # noqa
        self, philosopher: Philosopher, mock_sleep
    ):
        philosopher.state = PhilosopherState.EATING

        with mock.patch("dining_philosophers.forks.Fork.done"):
            philosopher.think()

            for fork in philosopher.forks:
                assert fork.done.called

        assert philosopher.state == PhilosopherState.THINKING

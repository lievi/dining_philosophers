from __future__ import annotations
from dataclasses import dataclass, field
import time
import threading
from typing import Dict

from constants import ForkState, PhilosopherState
# TODO: Adjust this circular import
from forks import Fork


class Philosopher(threading.Thread):
    def __init__(self, id) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.state = PhilosopherState.THINKING
        self.forks = Dict[int, Fork]

    def run(self):
        self.eat()

    def eat(self):
        fork_with_lowest_id = self.forks[min(self.forks.keys())]
        fork_with_highest_id = self.forks[max(self.forks.keys())]

        print(
            f'Philo. {self.id} trying to '
            f'acquire the fork with lowest id: {fork_with_lowest_id.id}\n'
        )
        try:
            fork_with_lowest_id.lock.acquire()
            print(
                f'Philo. {self.id} '
                f'acquired the fork id: {fork_with_lowest_id.id}\n'
            )
        except Exception as e:
            print(e)

        print(
            f'Philo. {self.id} trying to '
            f'acquire the fork with highest id: {fork_with_highest_id.id}\n'
        )
        try:
            fork_with_highest_id.lock.acquire()
            print(
                f'Philo. {self.id} '
                f'acquired the fork id: {fork_with_highest_id.id}\n'
            )
        except Exception as e:
            print(e)

        print(f'The Philo. {self.id} is eating\n')
        time.sleep(5)
        print(f'The Philo. {self.id} finished eating\n')
        fork_with_lowest_id.lock.release()
        fork_with_highest_id.lock.release()

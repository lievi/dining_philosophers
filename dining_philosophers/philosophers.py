from __future__ import annotations
import threading
from typing import Tuple

from dining_philosophers.exceptions import (
    PhilosopherWithMoreThanTwoForksException
)
from dining_philosophers.constants import PhilosopherState
from dining_philosophers.forks import Fork


class Philosopher(threading.Thread):
    def __init__(self, id: int, forks: Tuple[Fork, Fork]) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.state = PhilosopherState.THINKING
        if len(forks) > 2:
            raise PhilosopherWithMoreThanTwoForksException()
        self.forks = forks

    def run(self):
        self.eat()

    def eat(self):
        for fork in self.forks:
            fork.request(self)

        self.state = PhilosopherState.EATING

    def think(self):
        for fork in self.forks:
            fork.done()

        self.state = PhilosopherState.THINKING

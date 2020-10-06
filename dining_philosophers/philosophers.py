from __future__ import annotations
import threading
import time
from random import uniform
from typing import Tuple

from dining_philosophers.exceptions import (
    PhilosopherWithMoreThanTwoForksException,
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
        self.full = 3

    def run(self):
        while self.full > 1:
            self.eat()
            self.full -= 1
            self.think()
        print(f'{self} is full')
        return

    def eat(self):
        print(f'{self} is hungry, trying to eat')
        for fork in self.forks:
            fork.request(self)

        self.state = PhilosopherState.EATING
        print(f'{self} is eating')
        time.sleep(uniform(1.2, 5.0))

    def think(self):
        print(f'{self} is done eating, putting the forks down')
        for fork in self.forks:
            fork.done()

        self.state = PhilosopherState.THINKING
        time.sleep(uniform(1.2, 5.0))

    def __repr__(self) -> str:
        return f'Philosopher {self.id}'

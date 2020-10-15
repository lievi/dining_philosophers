from __future__ import annotations
import threading
import time
import logging
from random import uniform
from typing import Tuple

from dining_philosophers.constants import PhilosopherState
from dining_philosophers.forks import Fork

logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    EAT_TIMES_UNTIL_FULL = 3

    def __init__(self, id: int, forks: Tuple[Fork, Fork]) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.state = PhilosopherState.THINKING
        self.forks = forks
        self.full = 0

    def run(self):
        while self.full < self.EAT_TIMES_UNTIL_FULL:
            self.eat()
            self.full += 1
            self.think()
        logger.info(f'{self} is full')
        return

    def eat(self):
        logger.info(f'{self} is hungry, trying to eat')
        for fork in self.forks:
            fork.request(self)

        self.state = PhilosopherState.EATING
        logger.info(f'{self} is eating')
        time.sleep(uniform(1.2, 5.0))

    def think(self):
        logger.info(f'{self} is done eating, putting the forks down')
        for fork in self.forks:
            fork.done()

        self.state = PhilosopherState.THINKING
        time.sleep(uniform(1.2, 5.0))

    def __repr__(self) -> str:
        return f'Philosopher {self.id}'

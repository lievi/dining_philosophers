from __future__ import annotations
from dataclasses import dataclass, field
import threading
from typing import List

from constants import ForkState, PhilosopherState
# TODO: Adjust this circular import
from forks import Fork


class Philosopher(threading.Thread):
    def __init__(self, id) -> None:
        threading.Thread.__init__(self)
        self.id = id
        self.state = PhilosopherState.THINKING
        self.forks = List[Fork]

    def run(self):
        self.eat()

    def eat(self):
        ...

    def think(self):
        ...

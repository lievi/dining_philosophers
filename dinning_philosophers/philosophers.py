from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from dinning_philosophers.constants import PhilosopherState
from dinning_philosophers.forks import Fork


@dataclass
class Philosopher:
    id: int
    # TODO: Verify if make sense put only a list of neighbors
    left_neighbor: Philosopher = field(init=False)
    right_neighbor: Philosopher = field(init=False)
    state: PhilosopherState = field(
        init=False, default=PhilosopherState.THINKING
    )
    _fork: List[Fork] = field(init=False, default_factory=list)

    @property
    def fork(self) -> List[Fork]:
        return self._fork

    @fork.setter
    def fork(self, fork: Fork) -> None:
        if len(self._fork) < 2:
            self._fork.append(fork)

    def request_fork(self):
        # Verify if i had some dirty fork
        #
        ...

    def eat(self):
        ...

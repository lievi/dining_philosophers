from __future__ import annotations
import asyncio
from dataclasses import dataclass, field
import time
from typing import List

from constants import ForkState, PhilosopherState
# TODO: Adjust this circular import
from forks import Fork


@dataclass
class Philosopher:
    id: int
    # TODO: Verify if make sense put only a list of neighbors
    # left_neighbor: Philosopher = field(init=False)
    # right_neighbor: Philosopher = field(init=False)
    state: PhilosopherState = field(
        init=False, default=PhilosopherState.THINKING
    )
    forks: List[Fork] = field(init=False, default_factory=list)

    # @property
    # def fork(self) -> List[forks.Fork]:
    #     return self._forks

    # @fork.setter
    # def fork(self, fork: forks.Fork) -> None:
    #     if len(self._forks) < 2:
    #         self._forks.append(fork)

    async def eat(self):
        async with self.forks[0].lock, self.forks[1].lock:
            print(f'{self.id} get\'s both of the forks, starting to eat')
            asyncio.sleep(3)
            print(f'{self.id} done eating')

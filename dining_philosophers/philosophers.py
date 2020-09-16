from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from dining_philosophers.constants import ForkState, PhilosopherState
# TODO: Adjust this circular import
from dining_philosophers import forks


@dataclass
class Philosopher:
    id: int
    # TODO: Verify if make sense put only a list of neighbors
    # left_neighbor: Philosopher = field(init=False)
    # right_neighbor: Philosopher = field(init=False)
    state: PhilosopherState = field(
        init=False, default=PhilosopherState.THINKING
    )
    fork: List[forks.Fork] = field(init=False, default_factory=list)

    # @property
    # def fork(self) -> List[forks.Fork]:
    #     return self._forks

    # @fork.setter
    # def fork(self, fork: forks.Fork) -> None:
    #     if len(self._forks) < 2:
    #         self._forks.append(fork)

    def request_fork(self):
        # Verify if i had some dirty fork
        #
        ...

    def receive_request(self, neighbor: Philosopher, fork: forks.Fork) -> None:
        if self.state == PhilosopherState.THINKING:
            fork.state = ForkState.CLEAN
            fork.current_owner = neighbor

        if self.state == PhilosopherState.HUNGRY:
            if fork.state == ForkState.CLEAN:
                # Put in some queue
                ...
            fork.state = ForkState.CLEAN
            fork.current_owner = neighbor

    def eat(self):
        ...

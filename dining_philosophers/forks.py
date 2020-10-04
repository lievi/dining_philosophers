from __future__ import annotations
from dataclasses import dataclass, field
from threading import Lock, Condition
from typing import TYPE_CHECKING

from dining_philosophers.constants import ForkState

# The Philosopher class is just imported for type hinting
# I'm importing in that way to avoid cyclic import
if TYPE_CHECKING:
    from philosophers import Philosopher


@dataclass
class Fork:
    _owner: Philosopher = field(init=False)
    state: ForkState = field(init=False, default=ForkState.DIRTY)
    lock: Lock = field(init=False, default_factory=Lock)
    condition: Condition = field(init=False, default_factory=Condition)

    def request(self, philosopher: Philosopher):
        if self._owner == philosopher:
            print(f'The philosopher {philosopher} is already the owner')
        if self.state is ForkState.DIRTY:
            self.lock.acquire()
            self.state = ForkState.CLEAN
            self._owner = philosopher
            self.lock.release()

        if self.state is ForkState.CLEAN:
            with self.condition:
                self.condition.wait()

    def done(self):
        self.state = ForkState.DIRTY

        with self.condition:
            self.condition.notify_all()

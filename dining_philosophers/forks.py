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
    id: int
    _owner: Philosopher = field(init=False, default=None)
    state: ForkState = field(init=False, default=ForkState.DIRTY)
    lock: Lock = field(init=False, default_factory=Lock)
    condition: Condition = field(init=False, default_factory=Condition)

    def request(self, philosopher: Philosopher):
        if self._owner == philosopher:
            # TODO: Improve this set state with lock
            self.lock.acquire()
            print(
                f'{philosopher} is already the owner of {self}, clean it'
            )
            self.state = ForkState.CLEAN
            self.lock.release()
            return

        if self.state is ForkState.DIRTY:
            self.lock.acquire()
            print(
                    f'{philosopher} getting the dirty {self} from '
                    f'{self._owner}, and clean it'
                )
            self.state = ForkState.CLEAN
            self._owner = philosopher
            self.lock.release()
            return

        if self.state is ForkState.CLEAN:
            with self.condition:
                print(
                    f'{philosopher} is waiting the {self._owner} '
                    f'finish using the {self}'
                )
                self.condition.wait()

                self.lock.acquire()
                print(
                    f'{philosopher} getting ownership the {self} and clean it'
                )
                self._owner = philosopher
                self.state = ForkState.CLEAN
                self.lock.release()

    def done(self):
        self.state = ForkState.DIRTY

        with self.condition:
            self.lock.acquire()
            self.condition.notify_all()
            self.lock.release()

    def __repr__(self) -> str:
        return f'Fork {self.id}'

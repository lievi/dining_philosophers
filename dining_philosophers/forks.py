from __future__ import annotations
import logging
from dataclasses import dataclass, field
from threading import Lock, Condition
from typing import TYPE_CHECKING

from dining_philosophers.constants import ForkState

# The Philosopher class is just imported for type hinting
# I'm importing in that way to avoid cyclic import
if TYPE_CHECKING:
    from philosophers import Philosopher  # pragma: no cover

logger = logging.getLogger(__name__)


@dataclass
class Fork:
    id: int
    _owner: Philosopher = field(init=False, default=None)
    state: ForkState = field(init=False, default=ForkState.DIRTY)
    lock: Lock = field(init=False, default_factory=Lock)
    condition: Condition = field(init=False, default_factory=Condition)

    def request(self, philosopher: Philosopher):
        if self._owner == philosopher:
            with self.lock:
                logger.info(
                    f'{philosopher} is already the owner of {self}, clean it'
                )
                self.state = ForkState.CLEAN
                return

        if self.state is ForkState.DIRTY:
            with self.lock:
                logger.info(
                    f'{philosopher} getting the dirty {self} from '
                    f'{self._owner}, and clean it'
                )
                self.state = ForkState.CLEAN
                self._owner = philosopher
            return

        if self.state is ForkState.CLEAN:
            with self.condition:
                logger.info(
                    f'{philosopher} is waiting the {self._owner} '
                    f'finish using the {self}'
                )
                self.condition.wait()

                with self.lock:
                    logger.info(
                        f'{philosopher} getting ownership of '
                        f'{self} and clean it'
                    )
                    self._owner = philosopher
                    self.state = ForkState.CLEAN

    def done(self):
        with self.lock:
            self.state = ForkState.DIRTY

        with self.condition:
            self.condition.notify_all()

    def __repr__(self) -> str:
        return f'Fork {self.id}'

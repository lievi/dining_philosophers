from __future__ import annotations
from dataclasses import dataclass, field
from threading import Lock, Condition
from typing import TYPE_CHECKING

from constants import ForkState

# The Philosopher class is just imported for type hinting
# I'm importing in that way to avoid cyclic import
if TYPE_CHECKING:
    from philosophers import Philosopher


@dataclass
class Fork:
    owner: Philosopher
    state: ForkState = field(init=False, default=ForkState.DIRTY)
    lock: Lock = field(init=False, default_factory=Lock)
    condition: Condition = field(init=False, default_factory=Condition)

    def request(self, philosopher: Philosopher):
        ...

    def done(self):
        ...

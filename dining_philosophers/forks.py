from dataclasses import dataclass, field

from dining_philosophers.constants import ForkState
from dining_philosophers import philosophers


@dataclass
class Fork:
    state: ForkState = field(init=False, default=ForkState.DIRTY)
    current_owner: philosophers.Philosopher = field(init=False)

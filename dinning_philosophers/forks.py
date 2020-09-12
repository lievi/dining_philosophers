from dataclasses import dataclass, field

from dinning_philosophers.constants import ForkState


@dataclass
class Fork:
    state: ForkState = field(init=False, default=ForkState.DIRTY)

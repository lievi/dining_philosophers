from dataclasses import dataclass, field
from threading import Lock

# from dining_philosophers.constants import ForkState


@dataclass
class Fork:
    id: int
    lock: Lock = field(init=False, default_factory=Lock)

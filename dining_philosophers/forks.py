from dataclasses import dataclass, field
from asyncio import Lock

# from dining_philosophers.constants import ForkState


@dataclass
class Fork:
    lock: Lock = field(init=False, default_factory=Lock)

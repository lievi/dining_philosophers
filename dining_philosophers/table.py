import logging
from typing import List

from dining_philosophers.philosophers import Philosopher
from dining_philosophers.forks import Fork

logger = logging.getLogger(__name__)


class Table:
    """Class that prepare the philosophers and the forks in a correct way
    """
    PHILOSOPHERS_ON_TABLE = 5

    def start_dining(self):
        logger.info(
            f'Starting the dinner with {self.PHILOSOPHERS_ON_TABLE} '
            'philosophers'
        )
        forks = self._create_forks(self.PHILOSOPHERS_ON_TABLE)
        philosophers = self._create_philosophers(
            self.PHILOSOPHERS_ON_TABLE, forks
        )
        for philosopher in philosophers:
            philosopher.start()

    @staticmethod
    def _create_forks(number_of_philosophers: int) -> List[Fork]:
        return [Fork(i) for i in range(number_of_philosophers)]

    @staticmethod
    def _create_philosophers(
        number_of_philosophers: int, forks: List[Fork]
    ):
        philosophers = []

        for philosopher_number in range(number_of_philosophers):
            """
            Getting the neighbor forks.
            i'ts done by getting the remainder of the division of the current
            philosopher id and the next philosopher id
            by the number of philosophers

            So if the current philosopher id is 5 and the number o philo. on
            table is 5, the neighbors forks will be 5 and 0
            """
            neighbor_forks = (
                forks[philosopher_number % number_of_philosophers],
                forks[(philosopher_number + 1) % number_of_philosophers]
            )
            philosopher = Philosopher(philosopher_number, neighbor_forks)

            # Giving ownership to forks if no one is the owner
            for fork in neighbor_forks:
                if not fork._owner:
                    fork._owner = philosopher
            philosophers.append(philosopher)

        return philosophers

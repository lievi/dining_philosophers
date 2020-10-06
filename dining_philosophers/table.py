from typing import List

from dining_philosophers.philosophers import Philosopher
from dining_philosophers.forks import Fork

class Table:
    """Class that prepare the philosophers and the forks in a correct way
    """
    PHILOSOPHERS_ON_TABLE = 5

    def __init__(self) -> None:
        ...

    def start_dinning(self):
        print(
            f'Starting the dinner with {self.PHILOSOPHERS_ON_TABLE} '
            'philosophers'
        )
        forks = self.create_forks(self.PHILOSOPHERS_ON_TABLE)
        philosophers = self.create_philosophers(
            self.PHILOSOPHERS_ON_TABLE, forks
        )
        for philosopher in philosophers:
            philosopher.start()

    @staticmethod
    def create_forks(number_of_philosophers) -> List[Fork]:
        return [Fork(i) for i in range(number_of_philosophers)]

    @staticmethod
    def create_philosophers(number_of_philosophers, forks):
        philosophers = []

        for philosopher_number in range(number_of_philosophers):
            """
            Getting the neighbor forks.
            i'ts done by getting the remainder of the division of the current
            philosopher number and the next philosopher number
            by the number of philosophers
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

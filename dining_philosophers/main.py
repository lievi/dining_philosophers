from philosophers import Philosopher
from forks import Fork


def main():
    philosophers = []
    forks = []

    for i in range(4):
        forks.append(Fork(id=i))

    for i in range(4):
        p = Philosopher(i)
        last = ((i + 1) % 4)
        p.forks = {i: forks[i], last: forks[last]}
        philosophers.append(p)

    for p in philosophers:
        p.start()


main()

import asyncio
import time

from philosophers import Philosopher
from forks import Fork


async def main():
    fork0 = Fork()
    fork1 = Fork()
    fork2 = Fork()
    fork3 = Fork()

    p0 = Philosopher(0)
    p1 = Philosopher(1)
    p2 = Philosopher(2)
    p3 = Philosopher(3)

    p0.forks = [fork0, fork1]
    p1.forks = [fork1, fork2]
    p2.forks = [fork2, fork3]
    p3.forks = [fork3, fork0]

    await p0.eat()
    await p1.eat()
    await p2.eat()

asyncio.run(main())

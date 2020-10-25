# Dining Philosophers solution example

[![codecov](https://codecov.io/gh/lievi/dining_philosophers/branch/master/graph/badge.svg?token=YPhyGPUFL2)](undefined)

Chandy/Misra solution of the dining philosophers problem using python [threads](https://docs.python.org/3.8/library/threading.html#thread-objects), [Lock](https://docs.python.org/3.8/library/threading.html#lock-objects) and [Condition](https://docs.python.org/3.8/library/threading.html#condition-objects)
![alt dining philosophers problem](https://adit.io/imgs/dining_philosophers/at_the_table.png)

The Dining philosophers is a synchronization problem which is used to evaluate situations where there is a need of allocating multiple resources to multiple processes. The problem is:

Consider there are **five philosophers** sitting around a circular dining table. The dining table has **five forks** and a bowl of food in the middle.
At any instant, a philosopher is either **eating** or **thinking**. When a philosopher wants to eat, he uses *two forks* - one from their left and one from their right. When a philosopher wants to think, he keeps down both forks at their original place.
Eating is not limited by the remaining amounts of food;

## Solution
* The philosopher have a tuple of the neighbors forks
* The fork have a current **owner**
* A philosopher can only eat if he is owner of both neighbors forks
* When the philosopher wants to eat, he request the forks that he is not owner and waits until the others philosophers finish using it.
* When a philosopher finish eat, he change the state of the fork to **dirty**, and send a "signal" that he is finished eat.

For more information about the Chandy/Misra solution, please visit the references links.

## References
* https://www.stolaf.edu/people/rab/pdc/text/dpsolns.htm
* https://www.wikiwand.com/en/Dining_philosophers_problem
* https://www.tutorialspoint.com/dining-philosophers-problem-dpp#:~:text=The%20dining%20philosophers%20problem%20states,and%20left%20chopstick%20to%20eat.
* https://adit.io/posts/2013-05-11-The-Dining-Philosophers-Problem-With-Ron-Swanson.html

## How to use?
* Install de dependecies on pyproject.toml (generated using [poetry](https://python-poetry.org/))
* run the **main.py** file


## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Lievi Silva](https://github.com/lievi/dining_philosophers/blob/master/LICENSE)

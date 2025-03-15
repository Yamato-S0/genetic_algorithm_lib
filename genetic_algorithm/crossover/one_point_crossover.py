import random
from .base_crossover import BaseCrossover


class OnePointCrossover(BaseCrossover):
    """
    一点交叉
    """

    def crossover(self, parent1, parent2):
        length = len(parent1)
        point = random.randint(1, length - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

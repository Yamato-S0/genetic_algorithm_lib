from abc import ABC, abstractmethod


class BaseCrossover(ABC):
    """
    交叉手法の抽象クラス。
    2つの親個体(parent1, parent2)から1組または複数組の子個体を返す。
    """

    @abstractmethod
    def crossover(self, parent1, parent2):
        """
        :param parent1: first individual
        :param parent2: second individual
        :return: child1, child2 (two offspring)
        """

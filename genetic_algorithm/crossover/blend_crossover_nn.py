import numpy as np
from .base_crossover import BaseCrossover


class BlendCrossoverNN(BaseCrossover):
    """
    ニューラルネットワークの重みをブレンド交叉。
    """

    def __init__(self, alpha=0.5):
        self.alpha = alpha

    def crossover(self, parent1, parent2):
        """
        :param parent1: ニューラルネットの重み（辞書）
        :param parent2: ニューラルネットの重み（辞書）
        :return: 交叉後の新しい個体2つ
        """
        child1 = {}
        child2 = {}

        for key in parent1.keys():
            lower = np.minimum(parent1[key], parent2[key])
            upper = np.maximum(parent1[key], parent2[key])
            range_ = upper - lower

            child1[key] = np.random.uniform(
                lower - self.alpha * range_, upper + self.alpha * range_
            )
            child2[key] = np.random.uniform(
                lower - self.alpha * range_, upper + self.alpha * range_
            )

        return child1, child2

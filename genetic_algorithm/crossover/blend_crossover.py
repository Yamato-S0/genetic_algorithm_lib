import numpy as np
from .base_crossover import BaseCrossover


class BlendCrossover(BaseCrossover):
    """
    実数表現向けのブレンド交叉 (BLX-α)。
    """

    def __init__(self, alpha=0.5):
        """
        :param alpha: ブレンドの範囲 (デフォルト: 0.5)
        """
        self.alpha = alpha

    def crossover(self, parent1, parent2):
        """
        :param parent1: 実数ベクトル
        :param parent2: 実数ベクトル
        :return: 交叉後の子個体2つ
        """
        lower = np.minimum(parent1, parent2)
        upper = np.maximum(parent1, parent2)
        range_ = upper - lower
        child1 = np.random.uniform(
            lower - self.alpha * range_, upper + self.alpha * range_
        )
        child2 = np.random.uniform(
            lower - self.alpha * range_, upper + self.alpha * range_
        )
        return child1, child2

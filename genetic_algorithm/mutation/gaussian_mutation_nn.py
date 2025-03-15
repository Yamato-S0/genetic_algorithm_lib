import numpy as np
from .base_mutation import BaseMutation


class GaussianMutationNN(BaseMutation):
    """
    ニューラルネットワーク向けの突然変異手法。
    重みにガウスノイズを加える。
    """

    def __init__(self, mutation_rate=0.01, mu=0, sigma=1):
        self.mutation_rate = mutation_rate
        self.mu = mu
        self.sigma = sigma

    def mutate(self, individual):
        """
        :param individual: ニューラルネットワークの重み（辞書）
        :return: 突然変異後の重み
        """
        mutated = {}
        for key, value in individual.items():
            if np.random.random() < self.mutation_rate:
                mutated[key] = value + np.random.normal(
                    self.mu, self.sigma, value.shape
                )
            else:
                mutated[key] = value
        return mutated

import random
from .base_mutation import BaseMutation


class SwapMutation(BaseMutation):
    """
    順列表現向けの突然変異手法。
    2つのランダムな位置の要素を入れ替える。
    """

    def __init__(self, mutation_rate=0.1):
        self.mutation_rate = mutation_rate

    def mutate(self, individual):
        """
        :param individual: 順列（リスト）
        :return: 突然変異後の個体
        """
        mutated = individual.copy()
        if random.random() < self.mutation_rate:
            i, j = random.sample(
                range(len(mutated)), 2
            )  # 2つの異なるインデックスを選択
            mutated[i], mutated[j] = mutated[j], mutated[i]  # スワップ
        return mutated

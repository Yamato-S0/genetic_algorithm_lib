import random
from .base_mutation import BaseMutation


class SubtreeMutation(BaseMutation):
    """
    ツリー表現向けの突然変異手法。
    部分木をランダムに再生成する。
    """

    def __init__(self, mutation_rate=0.1, representation=None):
        """
        :param mutation_rate: 突然変異率
        :param representation: 既存の TreeRepresentation インスタンス
        """
        self.mutation_rate = mutation_rate
        self.representation = representation

    def mutate(self, individual):
        """
        :param individual: ツリーのルートノード
        :return: 突然変異後のツリー
        """

        def mutate_node(node, depth=0):
            if node is None:
                return None
            if random.random() < self.mutation_rate:
                return self.representation.random_individual(depth=depth)
            node.left = mutate_node(node.left, depth + 1)
            node.right = mutate_node(node.right, depth + 1)
            return node

        return mutate_node(individual)

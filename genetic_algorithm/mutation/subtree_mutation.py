import random
from genetic_algorithm.representations.tree_representation import (
    TreeRepresentation,
)
from .base_mutation import BaseMutation


class SubtreeMutation(BaseMutation):
    """
    ツリー表現向けの突然変異手法。
    部分木をランダムに再生成する。
    """

    def __init__(self, mutation_rate=0.1):
        self.mutation_rate = mutation_rate

    def mutate(self, individual):
        """
        :param individual: ツリーのルートノード
        :return: 突然変異後のツリー
        """

        def mutate_node(node, depth=0):
            if node is None:
                return None
            if random.random() < self.mutation_rate:
                return TreeRepresentation(max_depth=3).random_individual(
                    depth=depth
                )  # ランダム部分木
            node.left = mutate_node(node.left, depth + 1)
            node.right = mutate_node(node.right, depth + 1)
            return node

        return mutate_node(individual)

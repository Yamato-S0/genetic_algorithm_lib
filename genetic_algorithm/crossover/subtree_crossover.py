import random
from .base_crossover import BaseCrossover


class SubtreeCrossover(BaseCrossover):
    """
    ツリー表現向けの部分木交叉。
    """

    def crossover(self, parent1, parent2):
        """
        :param parent1: ツリーのルートノード
        :param parent2: ツリーのルートノード
        :return: 交叉後の子個体2つ
        """

        def get_random_subtree(node):
            if node is None or (node.left is None and node.right is None):
                return node
            return random.choice([node.left, node.right])

        # 部分木を交換
        subtree1 = get_random_subtree(parent1)
        subtree2 = get_random_subtree(parent2)

        child1 = parent1
        child2 = parent2

        child1.left = subtree2
        child2.left = subtree1

        return child1, child2

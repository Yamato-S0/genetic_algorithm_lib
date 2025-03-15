import random
from .base_crossover import BaseCrossover


class OrderCrossover(BaseCrossover):
    """
    順列表現向けのOrder Crossover (OX)。
    """

    def crossover(self, parent1, parent2):
        """
        :param parent1: 順列
        :param parent2: 順列
        :return: 交叉後の子個体2つ
        """
        size = len(parent1)
        p1, p2 = sorted(random.sample(range(size), 2))

        # 部分をコピー
        child1 = [-1] * size
        child1[p1:p2] = parent1[p1:p2]

        child2 = [-1] * size
        child2[p1:p2] = parent2[p1:p2]

        # 親から順番に埋めていく
        def fill(child, parent):
            pos = p2
            for gene in parent:
                if gene not in child:
                    if pos >= size:
                        pos = 0
                    child[pos] = gene
                    pos += 1
            return child

        return fill(child1, parent2), fill(child2, parent1)

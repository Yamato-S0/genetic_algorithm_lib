import random
from .base_representation import BaseRepresentation


class PermutationRepresentation(BaseRepresentation):
    """
    順列表現の個体を扱うクラス（例: 巡回セールスマン問題）。
    """

    def __init__(self, num_elements=10):
        """
        :param num_elements: 順列の要素数（デフォルト10）
        """
        self.num_elements = num_elements

    def random_individual(self):
        """
        :return: ランダムな順列（リスト）
        """
        return random.sample(range(self.num_elements), self.num_elements)

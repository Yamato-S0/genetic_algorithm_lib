import random
from .base_representation import BaseRepresentation


class RealRepresentation(BaseRepresentation):
    """
    実数表現の個体を扱うクラス。
    """

    def __init__(self, dimension=5):
        """
        :param dimension: 実数ベクトルの次元数（デフォルト5次元）
        """
        self.dimension = dimension

    def random_individual(self):
        """
        :return: ランダムな実数ベクトル（リスト）
        """
        return [random.random() for _ in range(self.dimension)]

import random
from .base_representation import BaseRepresentation


class BinaryRepresentation(BaseRepresentation):
    """
    バイナリ表現の個体を扱うクラス。
    """

    def __init__(self, length=10):
        """
        :param length: バイナリ列の長さ（デフォルト10ビット）
        """
        self.length = length

    def random_individual(self):
        """
        :return: ランダムな0,1列（文字列）
        """
        return "".join(random.choice(["0", "1"]) for _ in range(self.length))

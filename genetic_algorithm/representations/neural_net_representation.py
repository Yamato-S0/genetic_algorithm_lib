import numpy as np
from .base_representation import BaseRepresentation


class NeuralNetRepresentation(BaseRepresentation):
    """
    ニューラルネットワークの重みを遺伝的アルゴリズムで最適化するための表現。
    """

    def __init__(self, input_size=3, hidden_size=5, output_size=1):
        """
        :param input_size: 入力層のノード数
        :param hidden_size: 隠れ層のノード数
        :param output_size: 出力層のノード数
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

    def random_individual(self):
        """
        ランダムなニューラルネットワークの重みを生成する。
        """
        return {
            "W1": np.random.randn(
                self.input_size, self.hidden_size
            ),  # 入力層 → 隠れ層の重み
            "b1": np.random.randn(self.hidden_size),  # 隠れ層のバイアス
            "W2": np.random.randn(
                self.hidden_size, self.output_size
            ),  # 隠れ層 → 出力層の重み
            "b2": np.random.randn(self.output_size),  # 出力層のバイアス
        }

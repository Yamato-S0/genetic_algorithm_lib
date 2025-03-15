import random
from .base_representation import BaseRepresentation


class TreeNode:
    """
    木構造のノードクラス。
    各ノードは演算子または値を持つ。
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.left} {self.value} {self.right})"
        return str(self.value)


class TreeRepresentation(BaseRepresentation):
    """
    数式やルールベースの進化で使用される木構造の表現。
    """

    def __init__(self, max_depth=3, operators=None, terminals=None):
        """
        :param max_depth: 木の最大深さ
        :param operators: 使用可能な演算子リスト（デフォルト: +, -, *, /）
        :param terminals: 使用可能なターミナルノードのリスト（デフォルト: 0-9）
        """
        self.max_depth = max_depth
        self.operators = operators if operators else ["+", "-", "*", "/"]
        self.terminals = terminals if terminals else [str(i) for i in range(10)]

    def random_individual(self, depth=0):
        """
        ランダムな構文木（Expression Tree）を生成する。
        """
        if depth >= self.max_depth or (depth > 0 and random.random() < 0.3):
            # ターミナルノード（数字など）を生成
            return TreeNode(random.choice(self.terminals))

        # 内部ノード（演算子）を生成
        operator = random.choice(self.operators)
        left_child = self.random_individual(depth + 1)
        right_child = self.random_individual(depth + 1)
        return TreeNode(operator, left_child, right_child)

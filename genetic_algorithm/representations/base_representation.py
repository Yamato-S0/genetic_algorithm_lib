from abc import ABC, abstractmethod


class BaseRepresentation(ABC):
    """
    遺伝的アルゴリズムの個体を表現するための抽象クラス。
    すべての解表現（バイナリ、実数ベクトル、パーミュテーションなど）はこのクラスを継承する。
    """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """
        各表現（バイナリ, 実数ベクトルなど）のパラメータを受け取るコンストラクタ。
        """

    @abstractmethod
    def random_individual(self):
        """
        ランダムな個体を生成するメソッド。
        :return: ランダムな個体（データ型は派生クラスによる）
        """

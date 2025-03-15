from abc import ABC, abstractmethod


class BaseSelection(ABC):
    """
    選択手法の抽象クラス。
    エリート選択を選択手法の一部として統合する。
    """

    def __init__(self, elitism=0):
        """
        :param elitism: エリート選択で次世代にそのままコピーする個体数
        """
        self.elitism = elitism

    @abstractmethod
    def select(self, population, fitness_list):
        """
        :param population: 個体群 (list)
        :param fitness_list: 適合度リスト (list)
        :return: 次世代用に選ばれた個体群 (list)
        """

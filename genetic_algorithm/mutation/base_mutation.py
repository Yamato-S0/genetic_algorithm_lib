from abc import ABC, abstractmethod


class BaseMutation(ABC):
    """
    突然変異手法の抽象クラス。
    個体を受け取り、変異した個体を返す。
    """

    @abstractmethod
    def mutate(self, individual):
        """
        :param individual: individual to be mutated
        :return: mutated_individual
        """

import random
from .base_selection import BaseSelection


class TournamentSelection(BaseSelection):
    """
    トーナメント選択（エリート選択を含む）。
    複数の個体をランダムに選び、その中で最も適合度の高い個体を選択する。
    """

    def __init__(self, tournament_size=3, elitism=0):
        """
        :param tournament_size: トーナメントに参加する個体の数
        :param elitism: エリート選択で次世代にそのままコピーする個体数
        """
        super().__init__(elitism=elitism)
        self.tournament_size = tournament_size

    def select(self, population, fitness_list):
        """
        トーナメント選択を適用して次世代の個体を選択する。

        :param population: 現在の個体群
        :param fitness_list: 各個体の適合度リスト
        :return: 新しい個体群
        """
        assert len(fitness_list) == len(
            population
        ), "Mismatch in fitness_list and population lengths"

        # `fitness_list` に None や NaN がないか確認し、問題があればエラーを出す
        if any(
            fit is None or (isinstance(fit, float) and fit != fit)
            for fit in fitness_list
        ):
            raise ValueError(f"Invalid values in fitness_list: {fitness_list}")

        # (fitness, individual) のペアを作成
        fitness_individual_pairs = list(zip(fitness_list, population))

        # 適合度でソート (fitness をキーにする)
        sorted_population = [
            x[1]
            for x in sorted(
                fitness_individual_pairs, key=lambda pair: pair[0], reverse=True
            )
        ]

        # エリート選択
        new_population = sorted_population[: self.elitism]

        # トーナメント選択を実行
        while len(new_population) < len(population):
            tournament = random.sample(fitness_individual_pairs, self.tournament_size)
            winner = max(tournament, key=lambda pair: pair[0])[
                1
            ]  # 適合度が最も高い個体を選択
            new_population.append(winner)

        return new_population

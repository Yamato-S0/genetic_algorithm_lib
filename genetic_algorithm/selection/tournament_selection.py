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
        # エリート選択
        sorted_population = [
            x for _, x in sorted(zip(fitness_list, population), reverse=True)
        ]
        new_population = sorted_population[
            : self.elitism
        ]  # 上位N個の個体をそのままコピー

        # トーナメント選択を実行
        while len(new_population) < len(population):
            # ランダムに `tournament_size` 個の個体を選ぶ
            tournament = random.sample(
                list(zip(population, fitness_list)), self.tournament_size
            )
            # 適合度が最も高い個体を選択
            winner = max(tournament, key=lambda x: x[1])[0]
            new_population.append(winner)

        return new_population

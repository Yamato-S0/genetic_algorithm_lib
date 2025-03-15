import random
from genetic_algorithm.selection.base_selection import BaseSelection


class RouletteSelection(BaseSelection):
    """
    ルーレット選択
    """

    def select(self, population, fitness_list):
        # エリート選択
        sorted_population = [
            x for _, x in sorted(zip(fitness_list, population), reverse=True)
        ]
        new_population = sorted_population[
            : self.elitism
        ]  # 上位N個の個体をそのままコピー

        # ルーレットホイール選択を適用
        total_fitness = sum(fitness_list)
        while len(new_population) < len(population):
            pick = random.uniform(0, total_fitness)
            current = 0
            for individual, fitness in zip(population, fitness_list):
                current += fitness
                if current > pick:
                    new_population.append(individual)
                    break

        return new_population

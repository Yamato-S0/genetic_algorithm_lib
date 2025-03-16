import numpy as np
from genetic_algorithm.core import GeneticAlgorithm
from genetic_algorithm.selection import TournamentSelection
from genetic_algorithm.crossover import OrderCrossover
from genetic_algorithm.mutation import SwapMutation
from genetic_algorithm.representations.permutation_representation import (
    PermutationRepresentation,
)

# ランダムな都市の座標を生成
num_cities = 10
cities = np.random.rand(num_cities, 2)  # 2D座標


# TSPの適合度関数（距離を最小化）
def tsp_fitness(individual):
    total_distance = 0
    for i, city_index in enumerate(individual):
        city1 = cities[city_index]
        city2 = cities[
            individual[(i + 1) % len(individual)]
        ]  # 最後の都市から最初の都市へ戻る
        total_distance += np.linalg.norm(city1 - city2)
    return -total_distance  # 距離が短いほど適合度が高い


# GA 設定
tsp_representation = PermutationRepresentation(num_elements=num_cities)
selection = TournamentSelection(tournament_size=3, elitism=2)

ga = GeneticAlgorithm(
    representation_instance=tsp_representation,
    pop_size=50,
    selection=selection,
    crossover=OrderCrossover(),
    mutation=SwapMutation(mutation_rate=0.05),
    fitness_func=tsp_fitness,
)

# 実行
best_individual, best_fitness = ga.run(generations=200)
print("Best Route:", best_individual, "Distance:", -best_fitness)

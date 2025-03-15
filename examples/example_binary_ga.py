from genetic_algorithm.core import GeneticAlgorithm
from genetic_algorithm.selection import TournamentSelection
from genetic_algorithm.crossover import OnePointCrossover
from genetic_algorithm.mutation import BitFlipMutation
from genetic_algorithm.representations.binary_representation import (
    BinaryRepresentation,
)


# バイナリ個体の適合度関数: 1の数を最大化する
def binary_fitness(individual):
    return sum(int(bit) for bit in individual)


# GA 設定
binary_representation = BinaryRepresentation(length=20)
selection = TournamentSelection(tournament_size=3, elitism=2)

ga = GeneticAlgorithm(
    representation_class=binary_representation,
    pop_size=50,
    selection=selection,
    crossover=OnePointCrossover(),
    mutation=BitFlipMutation(mutation_rate=0.05),
    fitness_func=binary_fitness,
)

# 実行
best_individual, best_fitness = ga.run(generations=100)
print("Best:", best_individual, "Fitness:", best_fitness)

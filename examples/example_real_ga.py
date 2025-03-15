from genetic_algorithm.core import GeneticAlgorithm
from genetic_algorithm.selection import RouletteSelection
from genetic_algorithm.crossover import BlendCrossover
from genetic_algorithm.mutation import GaussianMutation
from genetic_algorithm.representations.real_representation import RealRepresentation


# 実数個体の適合度関数: すべての値の合計を最大化する
def real_fitness(individual):
    return sum(individual)


# GA 設定
real_representation = RealRepresentation(dimension=5)
selection = RouletteSelection(elitism=2)

ga = GeneticAlgorithm(
    representation_class=real_representation,
    pop_size=50,
    selection=selection,
    crossover=BlendCrossover(),
    mutation=GaussianMutation(mutation_rate=0.05),
    fitness_func=real_fitness,
)

# 実行
best_individual, best_fitness = ga.run(generations=100)
print("Best:", best_individual, "Fitness:", best_fitness)

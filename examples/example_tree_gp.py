from genetic_algorithm.core import GeneticAlgorithm
from genetic_algorithm.selection import TournamentSelection
from genetic_algorithm.crossover import SubtreeCrossover
from genetic_algorithm.mutation import SubtreeMutation
from genetic_algorithm.representations.tree_representation import TreeRepresentation


# ターゲット関数 (x^2 + 2x + 3)
def target_function(x):
    return x**2 + 2 * x + 3


# 適合度関数（ターゲット関数にどれだけ近いか）
def tree_fitness(individual):
    x_values = [0, 1, 2, 3, 4]
    error = sum(
        abs(eval(str(individual).replace("x", str(x))) - target_function(x))
        for x in x_values
    )
    return -error  # 誤差が小さいほど適合度が高い


# GA 設定
tree_representation = TreeRepresentation(
    max_depth=3, terminals=["x", "1", "2", "3", "4"]
)
selection = TournamentSelection(tournament_size=3, elitism=2)

ga = GeneticAlgorithm(
    representation_class=tree_representation,
    pop_size=50,
    selection=selection,
    crossover=SubtreeCrossover(),
    mutation=SubtreeMutation(mutation_rate=0.05),
    fitness_func=tree_fitness,
)

# 実行
best_individual, best_fitness = ga.run(generations=200)
print("Best Expression:", best_individual, "Fitness:", best_fitness)

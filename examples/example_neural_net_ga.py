import numpy as np
from genetic_algorithm.core import GeneticAlgorithm
from genetic_algorithm.selection import TournamentSelection
from genetic_algorithm.crossover import BlendCrossoverNN
from genetic_algorithm.mutation import GaussianMutationNN
from genetic_algorithm.representations.neural_net_representation import (
    NeuralNetRepresentation,
)


# ニューラルネットの適合度関数（最小二乗誤差を最小化）
def nn_fitness(individual):
    x = np.array([0.5, 0.2, 0.8])
    y_true = np.array([1.0])

    W1, b1, W2, b2 = (
        individual["W1"],
        individual["b1"],
        individual["W2"],
        individual["b2"],
    )
    hidden = np.tanh(np.dot(x, W1) + b1)
    output = np.dot(hidden, W2) + b2
    loss = np.mean((output - y_true) ** 2)

    return -loss  # 誤差が小さいほど適合度が高い


# GA 設定
nn_representation = NeuralNetRepresentation(input_size=3, hidden_size=5, output_size=1)
selection = TournamentSelection(tournament_size=3, elitism=2)

ga = GeneticAlgorithm(
    representation_instance=nn_representation,
    pop_size=50,
    selection=selection,
    crossover=BlendCrossoverNN(),
    mutation=GaussianMutationNN(mutation_rate=0.05),
    fitness_func=nn_fitness,
)

# 実行
best_individual, best_fitness = ga.run(generations=100)
print("Best Weights:", best_individual, "Fitness:", best_fitness)

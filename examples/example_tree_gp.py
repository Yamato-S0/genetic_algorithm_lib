import re
from genetic_algorithm.core import GeneticAlgorithm
from genetic_algorithm.selection import TournamentSelection
from genetic_algorithm.crossover import SubtreeCrossover
from genetic_algorithm.mutation import SubtreeMutation
from genetic_algorithm.representations.tree_representation import TreeRepresentation


# ターゲット関数 難し目
def target_function(x):
    return 2 * x**3 - 3 * x**2 + 4 * x - 1


def tree_fitness(individual):
    x_values = [0, 1, 2, 3, 4]
    error = 0

    for x in x_values:
        try:
            # 変数 x を適切に置換して式を作成
            expression = str(individual).replace("x", str(x))

            # 数式が安全なものかチェック（数値と基本演算子のみ許可）
            if not re.match(r"^[\d\s\+\-\*\/\(\)]+$", expression):
                raise ValueError(f"Unsafe expression: {expression}")

            predicted_value = eval(expression)  # 数式として評価
            error += abs(predicted_value - target_function(x))
        except Exception as e:
            # print(f"Error evaluating individual: {individual}, error: {e}")
            return -float("inf")  # エラーが発生した場合、大きな誤差を返す

    return -error  # 誤差が小さいほど適合度が高い


# GA 設定
tree_representation = TreeRepresentation(
    max_depth=3, terminals=["x", "1", "2", "3", "4"]
)
print(f"tree_representation instance: {tree_representation}")
print(f"Terminals in tree_representation: {tree_representation.terminals}")
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

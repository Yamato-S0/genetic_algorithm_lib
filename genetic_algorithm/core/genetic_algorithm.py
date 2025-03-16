import random


class GeneticAlgorithm:
    """
    遺伝的アルゴリズム(Genetic Algorithm)の実行クラス。
    selection, crossover, mutationはいずれもBaseクラスを実装したインスタンスを受け取る。
    """

    def __init__(
        self,
        representation_instance,
        pop_size=20,
        selection=None,
        crossover=None,
        mutation=None,
        fitness_func=None,
    ):
        """
        :param representation_instance: 実際に個体生成や評価を管理するクラス
        :param pop_size: 個体数
        :param selection: BaseSelectionを継承したインスタンス
        :param crossover: BaseCrossoverを継承したインスタンス
        :param mutation: BaseMutationを継承したインスタンス
        :param fitness_func: 評価関数(個体を入力にスカラーを返す関数)
        """
        self.representation_instance = representation_instance
        self.pop_size = pop_size
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.fitness_func = fitness_func

        # 初期集団を生成
        self.population = [
            self.representation_instance.random_individual()
            for _ in range(self.pop_size)
        ]

        self.fitness_list = [0] * self.pop_size

    def evaluate(self):
        """
        個体群を評価し、fitness_listに格納する。
        """
        for i, individual in enumerate(self.population):
            self.fitness_list[i] = self.fitness_func(individual)

    def step(self):
        """
        GAを1ステップ(世代交代)実行する。
        """
        # 評価
        self.evaluate()

        # 選択
        if self.selection:
            new_population = self.selection.select(self.population, self.fitness_list)
        else:
            new_population = random.choices(self.population, k=self.pop_size)

        # 交叉
        offspring = []
        for i in range(0, len(new_population), 2):
            parent1 = new_population[i]
            if i + 1 < len(new_population):
                parent2 = new_population[i + 1]
            else:
                parent2 = new_population[0]  # 端数が出たときの措置

            if self.crossover:
                child1, child2 = self.crossover.crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            offspring.append(child1)
            offspring.append(child2)

        # 次世代の個体を突然変異
        mutated_population = [
            self.mutation.mutate(ind) if self.mutation else ind for ind in offspring
        ]

        # 次世代集団へ置換
        self.population = mutated_population

    def run(self, generations=50):
        """
        指定世代数だけGAを実行する。
        """
        for gen in range(generations):
            self.step()
            self.evaluate()

            # 状況を出力（例：世代毎の最大適合度）
            max_fitness = max(self.fitness_list)
            print(f"Generation {gen+1}/{generations}, Max fitness: {max_fitness}")

        # 最終世代後の最良個体を返す
        best_fitness = max(self.fitness_list)
        best_individual = self.population[self.fitness_list.index(best_fitness)]
        return best_individual, best_fitness

import random
from .base_mutation import BaseMutation


class BitFlipMutation(BaseMutation):
    """
    ビットフリップ突然変異
    """

    def __init__(self, mutation_rate=0.01):
        self.mutation_rate = mutation_rate

    def mutate(self, individual):
        mutated = []
        for gene in individual:
            if random.random() < self.mutation_rate:
                mutated.append("1" if gene == "0" else "0")
            else:
                mutated.append(gene)
        return "".join(mutated)

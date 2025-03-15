import random
from .base_mutation import BaseMutation


class GaussianMutation(BaseMutation):
    """
    ガウシアン突然変異
    """

    def __init__(self, mutation_rate=0.01, mu=0, sigma=1):
        self.mutation_rate = mutation_rate
        self.mu = mu
        self.sigma = sigma

    def mutate(self, individual):
        mutated = []
        for gene in individual:
            if random.random() < self.mutation_rate:
                mutated_gene = gene + random.gauss(self.mu, self.sigma)
                mutated.append(mutated_gene)
            else:
                mutated.append(gene)
        return mutated

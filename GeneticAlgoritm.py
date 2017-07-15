import Numpy as np
from random import randint
queens = 8
mutation = 0,01
probabilidade = 0,02
class GeneticAlgoritm:

    def __init__(self):
        individuo = None



    #def createGeneration(queens):
     #   while 1

    def algGenetic(self, population, fnAdapt):
        while 1
            new_population = []
            for i in 7:
                x = self.seletionAleatoria(population, fnAdapt )
                y = self.seletionAleatoria(population,fnAdapt)
                child = self.reproduction(x,y)
                if mutation == probabilidade:
                    filho = self.mutation(filho)
                new_population.append(filho)
                population = new_population
        return population[0]

    def seletionAleatoria(self, population, fnAdapt):
        return  None

    def reproduction(self, crossX, crossY):
        n = randint(1,7)
        return crossX + crossY


    def mutation(self, filho):
        return filho
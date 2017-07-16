import Numpy as np
from random import randint
queens = 8
mutation = 0,01
probabilidade = 0,02
class GeneticAlgoritm:

    def __init__(self):
        tabuleiro = None
        avaliacao = None


    #def createGeneration(queens):
     #   while 1

    def algGenetic(self, population, fnAdapt):
        while 1:
            new_population = []
            for i in 7:
                x = self.seletionAleatoria(population, fnAdapt )
                y = self.seletionAleatoria(population,fnAdapt)
                child, child2 = self.reproduction(x,y)
                child.avaliacao = fnAdapt(child)
                child2.avaliacao = fnAdapt(child)
                child_F = None
                if(child.avaliacao >= child2.avaliacao):
                    child_F = child
                else:
                    child_F = child2
                if mutation == probabilidade:
                    child = self.mutation(child_F)
                new_population.append(child_F)
                population = new_population
        return population[0]

    def seletionAleatoria(self, population, fnAdapt):
        return  None

    def reproduction(self, crossX, crossY):
        n = randint(1,7)
        x = GeneticAlgoritm()
        y = GeneticAlgoritm()
        x.tabuleiro = []
        y.tabuleiro = []
        x.tabuleiro.extend(crossX.tabuleiro[0:n])
        x.tabuleiro.extend(crossY.tabuleiro[n:])
        y.tabuleiro.extend(crossX.tabuleiro[0:(crossX.length -1)-n])
        y.tabuleiro.extend(crossY.tabuleiro[(crossX.length -1)- n:])
        return x, y


    def mutation(self, filho):
        i = randint(0,7)
        x = randint(0,7)
        filho = filho.tabuleiro[i] = x
        return filho

    def fnAdapt(candidate):

        return 10
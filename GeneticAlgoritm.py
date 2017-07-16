from random import randint
import random

mutation = 0,01
probabilidade = 0,02
class GeneticAlgoritm:

    def __init__(self):
        tabuleiro = None
        avaliacao = None


    def createCross(queen):

        for i in 4:
            x = np.arange(queen)
            np.random.shuffle(x)
        return  x

    def createPol(self):
        population = []
        for i in 8:
            population.append(self.createCross(8))
        return population

    def algGenetic(self, population, fnAdapt):
        while 1:
            new_population = []
            for i in 7:
                x = self.seletionAleatoria(population, fnAdapt )
                y = self.seletionAleatoria(population,fnAdapt)
                child, child2 = self.reproduction(x,y)
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
        confrontos = 0
        col_confrontos = abs(len(candidate.tabuleiro) - len(np.unique(candidate.tabuleiro)))
        confrontos = confrontos + col_confrontos
        for i in range(len(candidate.tabuleiro)):
            for j in range(len(candidate.tabuleiro)):
                if (i != j):
                    dx = abs(i - j)
                    dy = abs(candidate.tabuleiro[i] - candidate.tabuleiro[j])
                    if (dx == dy):
                        confrontos += 1


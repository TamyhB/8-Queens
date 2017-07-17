import numpy as np
from random import randint
import random

mutation = 0.01
probabilidade = 0.02
queens = 8
class GeneticAlgoritm:

    def __init__(self):
        tabuleiro = None
        avaliacao = None

    def setAvaliacao(self, avaliacao):
        avaliacao = avaliacao

def createCross(queen):

    for i in range(1,4):
        x = np.arange(queen)
        np.random.shuffle(x)
    return  x

def createPol(x):
    population = []
    for i in range(0, x):
        x = GeneticAlgoritm()
        x.tabuleiro = createCross(8)
        av = fnAdapt(x)
        x.setAvaliacao(av)
        population.append(x)
    return population

def algGenetic(population):
    fnPopulation = []

    for i in range(0,7):
        x = seletionAleatoria(population)
        y = seletionAleatoria(population)
        print x
        print y
        child, child2 = reproduction(x,y)
        child_F = None
        if(child.avaliacao >= child2.avaliacao):
            child_F = child
        else:
            child_F = child2
        if mutation == probabilidade:
            child = mutation(child_F)
            fnPopulation.append(child_F)
        else:
            fnPopulation.append(child_F)
        population = fnPopulation
    x = min(fnPopulation)
    return population[fnPopulation.index(x)]

def seletionAleatoria(population):
    newPop = randint(0,len(population)-1)
    #print len(population)
    return  population[newPop]

def reproduction(crossX, crossY):
    x = GeneticAlgoritm()
    y = GeneticAlgoritm()
    print crossX
    print crossY
    tuplaSize = crossY.tabuleiro.shape
    n = tuplaSize[0] -1
    s = np.random.randint(n, size=1)
    aux_x = []
    aux_y = []
    aux_x.extend(crossX.tabuleiro[0:s[0]])
    aux_x.extend(crossY.tabuleiro[s[0]:])
    aux_y.extend(crossY.tabuleiro[0:s[0]])
    aux_y.extend(crossX.tabuleiro[s[0]:])
    x.tabuleiro = np.array(aux_x)
    y.tabuleiro = np.array(aux_y)
    #y.tabuleiro.extend(crossX.tabuleiro[0:(len(crossX.tabuleiro) - 1) - n])
    #y.tabuleiro.extend(crossY.tabuleiro[abs((len(crossX.tabuleiro) - 1) - n):])
    x.avaliacao = fnAdapt(x)
    y.avaliacao = fnAdapt(y)
    return x, y


def mutation(filho):
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

    return  confrontos

x = createPol(500)
result = algGenetic(x)
print result.tabuleiro
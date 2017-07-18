import numpy as np
from random import randint
import random

mutacao = 0.1
probabilidade = None
queens = 8

class GeneticAlgoritm:

    def __init__(self):
        tabuleiro = None
        avaliacao = None
        survival = None

    def setAvaliacao(self, avaliacao):
        avaliacao = avaliacao


def criar_cromossomo(queen):
    for i in range(1,8):
        x = np.arange(queen)
        np.random.shuffle(x)
    return  x


def create_populacao(x):
    population = []
    for i in range(0, x):
        x = GeneticAlgoritm()
        x.tabuleiro = criar_cromossomo(8)
        x.avaliacao = avaliar_confrontos_rainhas(x)
        population.append(x)
    return population


def minimo_vetor(vetor_populacao):
    menor = vetor_populacao[0]
    for individuo in vetor_populacao:
        if menor.avaliacao > individuo.avaliacao:
            menor = individuo
    return menor

# def maximo_vetor(vetor_populacao):
#     maximo = vetor_populacao[0]
#     for individuo in vetor_populacao:
#         if maximo.avaliacao < individuo.avaliacao:
#             maximo = individuo
#     return maximo

def algGenetic(population):
    nova_populacao = []
    while 1:
        for i in range(0,7):
            x = selecao_aleatoria_ponderada(population)
            while 1:
                y = selecao_aleatoria_ponderada(population)
                if y!=x:
                    break
            child, child2 = reproduction(x,y)
            best_child = None
            if(child.avaliacao <= child2.avaliacao):
                best_child = child
            else:
                best_child = child2
            probabilidade = random.random()
            print probabilidade
            if probabilidade <= mutacao:
                best_child = mutation(best_child)
                best_child.avaliacao = avaliar_confrontos_rainhas(best_child)
                nova_populacao.append(best_child)
            else:
                nova_populacao.append(best_child)
        population = nova_populacao
        individuo = minimo_vetor(nova_populacao)
        print "LEN POPULACAO " + str(len(population))
        print "MINIMO ATUAL " + str(individuo.avaliacao)
        print "MINIMO ATUAL " + str(individuo.tabuleiro)
        if individuo.avaliacao == 0:
            break
    return individuo

# def seletionAleatoria(population):
#     newPop = randint(0,len(population)-1)
#    # print  len(population)-1
#     print len(population)
#     print newPop
#     return  population[newPop]

def selecao_aleatoria_ponderada(population):
    faixa1 = []
    faixa2 = []
    faixa3 = []
    faixa4 = []

    for rainha in population:
        if rainha.avaliacao <= 7:
            faixa1.append(rainha)
        elif rainha.avaliacao <= 14:
            faixa2.append(rainha)
        elif rainha.avaliacao <= 21:
            faixa3.append(rainha)
        else:
            faixa4.append(rainha)

    while 1:
        dado_100_faces = randint(1, 100)

        if dado_100_faces <= 5:
            if len(faixa4) > 0:
                tamanho = len(faixa4) -1
                indice = randint(0, tamanho)
                return faixa4[indice]
        elif dado_100_faces <= 15 and dado_100_faces > 5:
            if len(faixa3) > 0:
                tamanho = len(faixa3) - 1
                indice = randint(0, tamanho)
                return faixa3[indice]
        elif dado_100_faces <= 45 and dado_100_faces > 15:
            if len(faixa2) > 0:
                tamanho = len(faixa2) - 1
                indice = randint(0,tamanho)
                return faixa2[indice]
        elif 100 >= dado_100_faces > 45:
            if len(faixa1) > 0:
                tamanho = len(faixa1) - 1
                indice = randint(0, tamanho)
                return faixa1[indice]



def reproduction(crossX, crossY):
    x = GeneticAlgoritm()
    y = GeneticAlgoritm()
    #print crossX.tabuleiro
    #print crossY.tabuleiro
    tuplaSize = crossY.tabuleiro.shape
    n = tuplaSize[0] - 1
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
    x.avaliacao = avaliar_confrontos_rainhas(x)
    y.avaliacao = avaliar_confrontos_rainhas(y)
    return x, y


def mutation(filho):
    print "Mutation!!!"
    i = randint(0,7)
    x = randint(0,7)
    filho.tabuleiro[i] = x
    return filho

def avaliar_confrontos_rainhas(candidate):
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

nova_populacao = create_populacao(100)
result = algGenetic(nova_populacao)
print result.tabuleiro
print result.avaliacao
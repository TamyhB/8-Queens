import numpy as np
from random import randint
import random
import sys

mutacao = 0.01
probabilidade = None
queens = 8
STOP_CTR = 0
MAX_ITER = 100000
POPULATION = None
class GeneticAlgoritm:

    def __init__(self):
        tabuleiro = None
        avaliacao = None
        survival = None

    def setAvaliacao(self, avaliacao):
        avaliacao = avaliacao


def criar_cromossomo(queen):
        x = np.arange(queen)
        np.random.shuffle(x)
        return  x


def criar_populacao(tamanho_populacao = 100):
    globals()

    population = [GeneticAlgoritm() for i in range(tamanho_populacao)]
    for i in range(0, tamanho_populacao):
        population[i].tabuleiro = criar_cromossomo(8)
        population[i].avaliacao = avaliar_ataque_rainhas(population[i])
    print len(population)

    return population


def minimo_vetor(vetor_populacao):
    globals()
    menor = vetor_populacao[0]
    for individuo in vetor_populacao:
        if menor.avaliacao > individuo.avaliacao:
            menor = individuo
    return menor

def selecao_aleatoria_ponderada(population):
    globals()
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
        dado_100_faces = np.random.randint(1, 100)

        if dado_100_faces <= 5:
            if len(faixa4) > 0:
                tamanho = len(faixa4)
                indice = np.random.randint(tamanho)
                return faixa4[indice]
        elif dado_100_faces <= 15 and dado_100_faces > 5:
            if len(faixa3) > 0:
                tamanho = len(faixa3)
                indice = np.random.randint(tamanho)
                return faixa3[indice]
        elif dado_100_faces <= 45 and dado_100_faces > 15:
            if len(faixa2) > 0:
                tamanho = len(faixa2)
                indice = np.random.randint(tamanho)
                return faixa2[indice]
        elif 100 >= dado_100_faces > 45:
            if len(faixa1) > 0:
                tamanho = len(faixa1)
                indice = np.random.randint(tamanho)
                return faixa1[indice]



def reproduction(crossX, crossY):
    globals()
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
    x.avaliacao = avaliar_ataque_rainhas(x)
    y.avaliacao = avaliar_ataque_rainhas(y)
    if x.avaliacao <= y.avaliacao:
        return x
    else:
        return y

def mutation(filho):
    globals()
    print "Mutation!!!"
    i = np.random.randint(len(filho.tabuleiro))
    x = np.random.randint(len(filho.tabuleiro))
    filho.tabuleiro[i] = x
    filho.avaliacao = avaliar_ataque_rainhas(filho)
    return filho

def avaliar_ataque_rainhas(candidate):
    globals()
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







def algoritmo_genetico(populacao):
    nova_populacao = []
    aux = minimo_vetor(populacao)
    print "Minimo POPULACAO " + str(aux.tabuleiro)
    for i in range(0,8):
        x = selecao_aleatoria_ponderada(populacao)
        while 1:
            y = selecao_aleatoria_ponderada(populacao)
            if y!=x:
                break
        child = reproduction(x,y)

        probabilidade = np.random.random()

        if probabilidade <= mutacao:
            print "probabilidade de mutacao " + str(probabilidade)
            child = mutation(child)
            nova_populacao.append(child)
        else:
            nova_populacao.append(child)
    populacao = nova_populacao
    return nova_populacao

def stop():
	globals()
	avaliacao_populacao = [pos.avaliacao for pos in population]
	if STOP_CTR in avaliacao_populacao:
		return True
	if MAX_ITER == iteration:
		return True
	return False

population = criar_populacao(1000)
iteration = 0;
while not stop():
	population = algoritmo_genetico(population)
	iteration +=1


print "Iteration number : ", iteration
for each in population:
    if each.avaliacao == 0:
        print each.tabuleiro


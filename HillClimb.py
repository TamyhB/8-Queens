import random
import time


possibleStatements = 0
changeStatements = 0
randomRestarts = 0

def randomBoard():
    items = [0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(items)
    return items

def stateQueens(state):
    value = 0
    for i in range(8):
        for j in range(8):
            if i != j and (abs(j-i) == abs(state[i] - state[j]) or state[i] == state[j]):
                value += 1

    return value/2

def nextMove(currentState, iteration):
    tempState = list(currentState)
    passIt = tempState[iteration]  # For same statement; current and next.
    bestValue = 28
    global possibleStatements

    for i in range(8):

        if i != passIt:
            tempState[iteration] = i
            currentValue = stateQueens(tempState)

            if currentValue < bestValue:
                bestValue = currentValue
                bestState = list(tempState)
            possibleStatements += 1

    return bestState, bestValue

def HillClimb(startState, nextMove, stateQueens):
    currentState = startState
    currentValue = stateQueens(currentState)

    global changeStatements
    global randomRestarts
    iteration = 0

    while True:

        nextState, nextValue = nextMove(currentState, iteration)
        if nextValue < currentValue:
            currentState = list(nextState)
            currentValue = nextValue
            changeStatements += 1

            if currentValue == 0:
                return currentState

        elif iteration == 7:
            randomRestarts += 1
            return HillClimb(randomBoard(), nextMove, stateQueens)


        iteration = (iteration + 1) % 8  # When 8 columns finish, iteration restarts


if __name__ == '__main__':

    startState = randomBoard()
    resultStatement = HillClimb(startState, nextMove, stateQueens)
    print "Result Statement:", resultStatement
    print "\nThe number of analyzed possible statements:", possibleStatements
    print "\nThe number of statement changes:", changeStatements
    print "\nThe number of random restarts:", randomRestarts




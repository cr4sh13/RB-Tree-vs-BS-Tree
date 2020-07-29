from ABR import *
from RB import *
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import random


# crea un albero binario di ricerca con n nodi random
def randomABR(n):
    A = []
    for i in range(n):
        A.append(i)
    random.shuffle(A)
    abrTree = ABR()
    for j in range(len(A)):
        abrTree.insert(A[j])
    return abrTree


# crea un albero rosso nero con n nodi random
def randomRB(n):
    A = []
    for i in range(n):
        A.append(i)
    random.shuffle(A)
    rbTree = RB()
    for j in range(len(A)):
        rbTree.insert(A[j])
    return rbTree


# esegue 200 iterazioni dello stesso problema su diversi alberi da n
# nodi e nel calcola la media dei tempi
def timeTreeSearch(n):
    ABRTime = []
    RBTime = []

    for i in range(200):
        abrTree = randomABR(n)
        rbTree = randomRB(n)

        start = timer()
        abrTree.treeSearch(abrTree.root, random.randint(1, n))
        end = timer()
        time = end - start
        ABRTime.append(time)

        start = timer()
        rbTree.treeSearch(rbTree.root, random.randint(1, n))
        end = timer()
        time = end - start
        RBTime.append(time)

    mediaABR = 0
    for j in range(len(ABRTime)):
        mediaABR += ABRTime[j]
    mediaABR = mediaABR / 200

    mediaRB = 0
    for k in range(len(RBTime)):
        mediaRB += RBTime[k]
    mediaRB = mediaRB / 200

    return mediaABR, mediaRB


def testTreeSearch():
    pltABR = []
    pltRB = []
    n = 5
    X = []

    while n <= 1000:
        mediaABR, mediaRB = timeTreeSearch(n)
        pltABR.append(mediaABR)
        pltRB.append(mediaRB)
        X.append(n)
        n += 5

    plt.figure()
    plt.plot(X, pltABR, 'r', label='ABR')
    plt.plot(X, pltRB, 'b', label='RB')
    plt.xlabel('Numero nodi')
    plt.ylabel('Tempo impiegato')
    plt.legend(loc='upper left')
    plt.show()


# esegue 200 iterazioni dello stesso problema su diversi alberi da n
# nodi e nel calcola la media dei tempi
def timeInOrder(n):
    ABRTime = []
    RBTime = []

    for i in range(200):
        abrTree = randomABR(n)
        rbTree = randomRB(n)

        start = timer()
        abrTree.inOrder(abrTree.root)
        end = timer()
        time = end - start
        ABRTime.append(time)

        start = timer()
        rbTree.inOrder(rbTree.root)
        end = timer()
        time = end - start
        RBTime.append(time)

    mediaABR = 0
    for j in range(len(ABRTime)):
        mediaABR += ABRTime[j]
    mediaABR = mediaABR / 200

    mediaRB = 0
    for k in range(len(RBTime)):
        mediaRB += RBTime[k]
    mediaRB = mediaRB / 200

    return mediaABR, mediaRB


def testInOrder():
    pltABR = []
    pltRB = []
    n = 5
    X = []

    while n <= 1000:
        mediaABR, mediaRB = timeInOrder(n)
        pltABR.append(mediaABR)
        pltRB.append(mediaRB)
        X.append(n)
        n += 5

    plt.figure()
    plt.plot(X, pltABR, 'r', label='ABR')
    plt.plot(X, pltRB, 'b', label='RB')
    plt.xlabel('Numero nodi')
    plt.ylabel('Tempo impiegato')
    plt.legend(loc='upper left')
    plt.show()


# esegue 200 iterazioni dello stesso problema su diversi alberi da n
# nodi e nel calcola la media dei tempi
def timeInsert(n):
    ABRTime = []
    RBTime = []
    abrTree = ABR()
    rbTree = RB()

    for i in range(200):
        A = []

        for j in range(n):
            A.append(j)
        random.shuffle(A)

        start = timer()
        for k in range(len(A)):
            abrTree.insert(A[k])
        end = timer()
        time = end - start
        ABRTime.append(time)

        start = timer()
        for c in range(len(A)):
            rbTree.insert(A[c])
        end = timer()
        time = end - start
        RBTime.append(time)

    mediaABR = 0
    for j in range(len(ABRTime)):
        mediaABR += ABRTime[j]
    mediaABR = mediaABR / 200

    mediaRB = 0
    for k in range(len(RBTime)):
        mediaRB += RBTime[k]
    mediaRB = mediaRB / 200

    return mediaABR, mediaRB


def testInsert():
    pltABR = []
    pltRB = []
    n = 5
    X = []

    while n <= 1000:
        mediaABR, mediaRB = timeInsert(n)
        pltABR.append(mediaABR)
        pltRB.append(mediaRB)
        X.append(n)
        n += 5

    plt.figure()
    plt.plot(X, pltABR, 'r', label='ABR')
    plt.plot(X, pltRB, 'b', label='RB')
    plt.xlabel('Elemanti da inserire')
    plt.ylabel('Tempo impiegato')
    plt.legend(loc='upper left')
    plt.show()

# testInsert()
# testInOrder()
# testTreeSearch()

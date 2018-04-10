import random
import copy
import numpy as np
from time import *

cuts = []
graph = {}

def getRandomEdge(graph):
    v = random.choice(list(graph.keys()))
    w = random.choice(graph[v])
    return (v,w)

def kargerMinCut(graph):
    while len(graph) > 2:
        v, w = getRandomEdge(graph)
        contract(graph, v, w)
    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)

def contract(graph, v, w):
    for node in graph[w]:
        if node != v:
            graph[v].append(node)
        graph[node].remove(w)
        if node != v:
            graph[node].append(v)
    del graph[w]

def readGraphFromFile(filename):
    file = open(filename)
    global graph
    graph = {}
    for line in file:
        edges = []
        line = line.split()
        line = [int(x) for x in line]
        graph[int(line[0])] = line[1:]
    print(str(len(graph)) + " vertices in dictionary.")
    return graph

def main():
    start = time()
    iteration = 10

    # graph = readGraphFromFile('kargerMinCut.txt')
    graph = readGraphFromFile('sample.txt')
    for i in range(1, iteration):
        copiedGraph = copy.deepcopy(graph)
        kargerMinCut(copiedGraph)
    print("MinCut is " + str(min(cuts)))
    pass
    end = time()
    print("Time taken by the algorithm after {0} iteration(s) is {1} ".format( iteration,str(end - start)))

main()

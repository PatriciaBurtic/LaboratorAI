from GA import *
from utils import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings
import os

net = readDataFromGML('lesmis.gml')
gaParam = {"popSize": 300, "noGen": 4, "pc": 0.8, "pm": 0.1, "network": net}
problParam = {'function': modularity, 'retea': net}

def getData(x):
    comunities = []
    for index in range(0, problParam['retea']['noNodes']+1):
        comunities.append([])
    for index in range(0, net['noNodes']):
        comunities[x[index]].append(index + 1)
    index = 0
    while index < len(comunities):
        if comunities[index] == []:
            comunities.pop(index)
        else:
            index += 1
    return comunities

def main():
    warnings.simplefilter('ignore')
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    inProgress = True
    g = -1
    while (inProgress and g < gaParam['noGen']):
        g += 1
        ga.oneGeneration()

        bestChromosome = ga.bestChromosome()
        data=getData(bestChromosome.repres)
        print('------------------------------------------')
        print('Generation ' + str(g) +  '\nFitness: ' + str(
            bestChromosome.fitness) + ' ' + '\nNo of comunities:' + str(len(data)))

    
    A = np.matrix(net["mat"])
    G = nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G) 
    plt.figure(figsize=(8, 8))
    nx.draw_networkx_nodes(G, pos, node_size=200, cmap=plt.cm.RdYlBu, node_color = ga.population[0].repres)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()


main()

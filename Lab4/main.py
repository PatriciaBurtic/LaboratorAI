from GA import GA
import numpy as np 
import matplotlib.pyplot as plt 
import warnings 
import math
from utils import readData, modularity,readDataTSP, readDataSpace

mat = []
#noNodes,mat = readData(mat,'easy_01_tsp.txt')
#noNodes,mat = readDataSpace(mat,'medium_01_tsp.txt')
noNodes,mat = readDataTSP('bays29.tsp')
#noNodes,mat = readDataTSP('ulysses16.tsp')

gaParam = {"popSize": 100, "noGen": 400, "network": mat}
problParam = {'function': modularity, 'retea': mat,'noNodes':noNodes}

if __name__ == "__main__":
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    
   
    for g in range(gaParam['noGen']):
      
        ga.oneGenerationElitism()
        bestChromo = ga.bestChromosome()
        
        print("----------------------------------")
        print(bestChromo)
        
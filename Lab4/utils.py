from random import randint
from p2 import *

def generatePermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    pos3 = randint(0, n - 1)
    pos4 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    perm[pos3], perm[pos4] = perm[pos4], perm[pos3]
    return perm

def readData(mat, fileName):
  
    matrix=[]
   
    f = open(fileName,'r')
    n = int(f.readline())
    for _ in range(n):   
        linie = [int(num) for num in f.readline().split(',')]
        matrix.append(linie)

    return n,matrix

def readDataSpace(mat, fileName):
  
    matrix=[]
   
    f = open(fileName,'r')
    n = int(f.readline())
    for _ in range(n):   
        linie = [int(num) for num in f.readline().split('  ')]
        matrix.append(linie)

    return n,matrix

 
def modularity(comm, mat):
    cost=0
    for i in range(len(comm)-1):
        cost+=mat[comm[i]][comm[i+1]]
    cost+=mat[comm[len(comm)-1]][comm[0]]
   
    return cost

def readDataTSP(filename):
    matrix=[]
    coords = {}
   
    f = open(filename,'r')
    line = f.readline()
    while(line!="EOF"):
        data = line.split()
        coords[int(data[0])] = (float(data[1]),float(data[2]))
        line = f.readline()
    
    n=0
    for key in coords.keys():
        n=key
    
    for i in range(1,n+1):
        line = []
        for j in range(1,n+1):
            coordI = coords[i]
            coordJ = coords[j]
            distIJ = distantaEuclidiana(coordI[0],coordI[1],coordJ[0],coordJ[1])
            line.append(distIJ)
        matrix.append(line)
    
    return n,matrix









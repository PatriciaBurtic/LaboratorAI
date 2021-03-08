import sys


def minimumDistance(noCities, distances, currentPath):
    currentMinimum = sys.maxsize
    currentCity = -sys.maxsize -1
    cities = range(1,n+1)

    for city in cities:
        distance = distances[city-1]
        if distance < currentMinimum and city not in currentPath and distance != 0:
            currentCity = city
            currentMinimum =  distances[city-1]
    
    return currentCity, currentMinimum
            


def searchShortestPath(noCities,source,destination,matrix):
    cost = 0
    path = [source]
    
    while len(path) != noCities:
        city, minDist = minimumDistance(noCities, matrix[path[-1]-1], path)
        cost += minDist
        path.append(city)

        if city == destination:
            break
    
    if source == destination:
        cost += matrix[path[-1]-1][source - 1]
    
    return path, cost


def visitAllCities(n, matrix):
    minimumCost = sys.maxsize
    shortestPath = []

    for city in range(1,n+1):
        path,cost = searchShortestPath(n,city,city,matrix)
        if cost < minimumCost:
            minimumCost = cost
            shortestPath = path
    
    return minimumCost, shortestPath

def sourceToDestination(n, source, destination, matrix):
    shortestPath, minimumCost = searchShortestPath(n,source,destination,matrix)
    return minimumCost, shortestPath

    

if __name__ == '__main__':
    matrix=[]
    f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\easy_01_tsp.txt",'r')
    #f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\medium_01_tsp.txt",'r')
    #f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\hard_01_tsp.txt",'r')
    n = int(f.readline())
    for i in range(n):   
        linie = [int(num) for num in f.readline().split(',')]
        matrix.append(linie)
    source = int(f.readline())
    destination = int(f.readline())   
    
    f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\easy_01_my_solution.txt",'w')

    minimumCost, shortestPath = visitAllCities(n,matrix)
    
    f.write(str(len(shortestPath)))
    f.write('\n')
    f.write(str(shortestPath))
    f.write('\n')
    f.write(str(minimumCost))
    f.write('\n')

    minimumCost, shortestPath = sourceToDestination(n,source,destination,matrix)

    f.write(str(len(shortestPath)))
    f.write('\n')
    f.write(str(shortestPath))
    f.write('\n')
    f.write(str(minimumCost))









    
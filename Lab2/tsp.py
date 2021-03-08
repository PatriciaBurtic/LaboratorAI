import sys


def minimumDistance(noCities, distances, currentPath):
    currentMinimum = sys.maxsize
    currentCity = -sys.maxsize -1
    cities = range(1,n+1)

    #search nearest neighbour which is not already in the path
    for city in cities:
        distance = distances[city-1]
        if distance < currentMinimum and city not in currentPath and distance != 0:
            currentCity = city
            currentMinimum =  distances[city-1]
    
    #return nearest neighbour and the cost to travel to it
    return currentCity, currentMinimum
            


def searchShortestPath(noCities,source,destination,matrix):
    cost = 0
    path = [source]
    
    #search a path to destination until we reach it or the length of the path is equal to the initial number of cities
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
    #visit all cities and return the path and its cost, from city number 1 
    path,cost = searchShortestPath(n,1,1,matrix)
    return cost, path

def sourceToDestination(n, source, destination, matrix):
    #find shortest path from a specific source to a specific destination and its cost
    shortestPath, minimumCost = searchShortestPath(n,source,destination,matrix)
    return minimumCost, shortestPath

    

if __name__ == '__main__':
    matrix=[]
    #f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\easy_01_tsp.txt",'r')
    #f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\medium_01_tsp.txt",'r')
    f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\hard_01_tsp.txt",'r')
    n = int(f.readline())
    for i in range(n):   
        linie = [int(num) for num in f.readline().split(',')]
        matrix.append(linie)
    source = int(f.readline())
    destination = int(f.readline())   
    
    f = open("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab2\\my_solution.txt",'w')

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









    
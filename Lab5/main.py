from utils import readData
from aco import ACO, World
from plot import plot


if __name__ == '__main__':
    
    #noCities, cost_matrix, points = readData("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab5\\ulysses16.txt")
    noCities, cost_matrix, points = readData("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab5\\data.txt")
    #noCities, cost_matrix, points = readData("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab5\\data2.txt")
    #noCities, cost_matrix, points = readData("D:\\UBB_info_sem_4\\AI\\LAB\\Teme\\Lab5\\data3.txt")
    
    paramACO = {"ant_count":10, "generations":100, "alpha":1.0, "beta": 10.0, "rho":0.5, "q":10}
    paramWorld = {"cost_matrix":cost_matrix,"noCities":noCities}

    aco = ACO(paramACO)
    graph = World(paramWorld)

    path, cost = aco.solve(graph)
    print("\n")
    print("\n")
    print("BEST: Cost: "+str(cost)+" \nPath: "+str(path))
    plot(points, path)
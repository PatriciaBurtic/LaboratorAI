import math

def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def readData(filename):
    cities = []
    points = []
    with open(filename,'r') as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=float(city[1]), y=float(city[2])))
            points.append((float(city[1]), float(city[2])))
    cost_matrix = []
    noCities = len(cities)
    for i in range(noCities):
        row = []
        for j in range(noCities):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    return noCities, cost_matrix, points
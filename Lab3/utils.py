from random import randint
import networkx as nx

def generateNewRandomValue(number1, number2):
    return randint(number1, number2)

def representation(ret):
    repres = [generateNewRandomValue(0, ret['noNodes'] - 1) for _ in range(ret['noNodes'])]
    return repres

def readDataFromGML(filename):
    G = nx.read_gml(filename, label='id')

    net = {}
    net['noNodes'] = G.number_of_nodes()
    net['mat'] = nx.adjacency_matrix(G).todense()
    net['noEdges'] = G.number_of_edges()
    net['degrees'] = [val for (node, val) in G.degree()]
    net['graph'] = G
    return net

def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for index in range(0, noNodes):
        for secondIndex in range(0, noNodes):
            if (communities[index] == communities[secondIndex]):
                Q += (mat.item(index, secondIndex) - degrees[index] * degrees[secondIndex] / M)
    return Q * 1 / M


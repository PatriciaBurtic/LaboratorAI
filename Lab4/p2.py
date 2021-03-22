import math

def distantaEuclidiana(x1,y1,x2,y2):
    #Complexitate O(1)
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def test():
    assert distantaEuclidiana(1,5,4,1) == 5.0
    assert distantaEuclidiana(1,5,4,1) != 5.1

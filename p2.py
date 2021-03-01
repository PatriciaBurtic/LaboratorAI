import math

def distantaEuclidiana(x1,y1,x2,y2):
    #Complexitate O(1)
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def test():
    assert distantaEuclidiana(1,5,4,1) == 5.0
    assert distantaEuclidiana(1,5,4,1) != 5.1

if __name__ == '__main__': 
    test()
    print(">>Dati coordonatele primului punct")
    x1 = int(input("x="))
    y1= int(input("y="))

    print(">>Dati coordonatele celui de-al doilea punct.")
    x2 = int(input("x="))
    y2= int(input("y="))

    dist = distantaEuclidiana(x1,y1,x2,y2)
    print("Distanta euclidiana intre punctele ("+str(x1)+","+str(y1)+") si ("+str(x2)+","+str(y2)+") este "+str(dist))
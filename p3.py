def produs(v1,v2):
    #Complexitate O(n)
    s = 0
    for x,y in zip(v1,v2):
        if x!=0 and y!=0:
            s += x*y
    return s

def parseazaSirInt(sir):
    #Complexitate O(n)
    for numar in sir:
        if numar.isnumeric() == False:
            return False
    return True

def transformaInInt(v):
    #Complexitate O(n)
    vInt = []
    for string in v:
        vInt.append(int(string))
    return vInt

def calculeazaProdusVectori(v1,v2):
    #Complexitate O(n)
    vector1 = v1.split(" ")
    vector2 = v2.split(" ")
    if parseazaSirInt(vector1) == False or parseazaSirInt(vector2) == False:
        raise Exception("Sirurile trebuie sa contina doar numere naturale despartite printr-un singur spatiu!")
    return produs(transformaInInt(vector1),transformaInInt(vector2))


def test():
    assert calculeazaProdusVectori("1 0 2 0 3", "1 2 0 3 1") == 4
    assert calculeazaProdusVectori("1 1 2 0 3", "1 2 0 3 1") == 6
    try:
        calculeazaProdusVectori("1  1 2 3", "1 2 3 4")
    except Exception:
        assert True
    try:
        calculeazaProdusVectori("1 A 2 3", "1 2 3 4")
    except Exception:
        assert True
    try:
        calculeazaProdusVectori("1 2 2 3", "1 A 3 4")
    except Exception:
        assert True


if __name__ == '__main__':
    test()
    v1 = input(">>Dati primul sir de numere naturale despartite printr-un singur spatiu:")
    v2 = input(">>Dati al doilea sir de numere naturale despartite printr-un singur spatiu:")
    try:
        produs = calculeazaProdusVectori(v1,v2)
        print("Produsul celor doi vectori este "+str(produs))
    except Exception as e:
        print(e)

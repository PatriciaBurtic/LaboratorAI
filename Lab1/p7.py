def maxK(sir,k):
    #Complexitate O(max(nlog n, k))
    sir.sort(reverse=True)
    i=0
    while k > 1:
        if sir[i] != sir[i+1]:
            k = k-1
        i = i+1

    return sir[i]

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

def gasesteKMax(sir,k):
    #Complexitate O(n)
    sirSplit = sir.split(" ")
    if parseazaSirInt(sirSplit) == False:
        raise Exception("Sirul trebuie sa contina doar numere naturale separate printr-un singur spatiu!")
    return maxK(transformaInInt(sirSplit),k)

def test():
    assert gasesteKMax("7 4 6 3 9 1",2) == 7
    assert gasesteKMax("7 4 6 3 9 1",2) != 9
    assert gasesteKMax("7 4 6 3 9 1",3) == 6
    try:
        gasesteKMax("7 4 6 3 9  1",3)
    except Exception:
        assert True
    try:
        gasesteKMax("7 4 6 3 9 A",3)
    except Exception:
        assert True

if __name__ == '__main__':
    test()
    v = input(">>Dati sirul de numere naturale despartite printr-un singur spatiu: ")
    k = int(input(">>Dati al catelea maxim doriti sa il aflati: "))
    try:
        print(gasesteKMax(v,k))
    except Exception as e:
        print(e)
    
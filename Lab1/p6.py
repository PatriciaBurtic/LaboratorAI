def elementMajoritar(sir):
    return [i for i in sir if sir.count(i)>=len(sir)//2][0]

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

def gasesteElementMajoritar(sir):
    #Complexitate O(n)
    sirSplit = sir.split(" ")
    if parseazaSirInt(sirSplit) == False:
        raise Exception("Sirul trebuie sa contina doar numere naturale separate printr-un singur spatiu!")
    return elementMajoritar(transformaInInt(sirSplit))

def test():
    assert gasesteElementMajoritar("2 8 7 2 2 5 2 3 1 2 2") == 2
    assert gasesteElementMajoritar("2 8 7 2 2 5 2 3 1 2 2") != 5
    try:
        gasesteElementMajoritar("7 4 6 3 9  1")
    except Exception:
        assert True
    try:
        gasesteElementMajoritar("7 4 6 3 9 A")
    except Exception:
        assert True


if __name__ == '__main__':
    test()
    v = input(">>Dati sirul de numere naturale despartite printr-un singur spatiu: ")
    try:
        print(gasesteElementMajoritar(v))
    except Exception as e:
        print(e)

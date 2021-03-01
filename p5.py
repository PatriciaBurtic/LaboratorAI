def cauta(sir):
    #Complexitate O(n)
    if sir[0] in sir[1:]:
        return sir[0]
    else:
        return cauta(sir[1:])

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

def cautaSiVerifica(sir):
    #Complexitate O(n)
    sirSplit = sir.split(" ")
    if parseazaSirInt(sirSplit) == False:
        raise Exception("Sirul trebuie sa contina doar numere naturale separate printr-un singur spatiu!")
    return cauta(transformaInInt(sirSplit))

def test():
    assert cautaSiVerifica("1 2 3 4 2") == 2
    assert cautaSiVerifica("1 2 3 3 4") == 3
    try:
        cautaSiVerifica("1  2 3 4")
    except Exception:
        assert True
    try:
        cautaSiVerifica("1 A 3 4")
    except Exception:
        assert True

if __name__ == '__main__':
    test()
    v = input(">>Dati sirul de numere naturale despartite printr-un singur spatiu:")
    try:
        print(cautaSiVerifica(v))
    except Exception as e:
        print(e)

    
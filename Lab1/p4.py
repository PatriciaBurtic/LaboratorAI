def cautaSingle(sirInitial):
    #Complexitate O(n)
    sir = sirInitial.split(" ")
    dict = {}

    for cuvant in sir:
        if cuvant in dict:
            dict[cuvant] = dict[cuvant]+1
        else:
            dict[cuvant]=1
    
    rezultat = ""
    for cuvant in dict:
        if dict[cuvant] == 1:
            rezultat = rezultat + cuvant + " "
        
    return rezultat

def test():
    assert cautaSingle("Ana are mere") == "Ana are mere "
    assert cautaSingle("Ana Ana are are mere") == "mere "
    assert cautaSingle("Ana are mere") != "mere"


if __name__ == '__main__': 
    test()
    sirInitial = input(">>Dati o propozitie: ")
    print(cautaSingle(sirInitial))



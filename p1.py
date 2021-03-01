def gasesteMaximLexicografic1(sirInitial):
    #Complexitate O(n)
    sir = sirInitial.split(" ")
    maxim = sir[0]
    for cuvant in sir:
        if cuvant > maxim:
            maxim = cuvant
    return maxim

def gasesteMaximLexicografic2(sirInitial):
    #Complexitate O(n*log n)
    sir = sirInitial.split(" ")
    sir.sort(reverse=True)
    return sir[0]


def test():
    assert gasesteMaximLexicografic1("Ana are mere si pere") == "si"
    assert gasesteMaximLexicografic2("Ana are mere si pere") == "si"
    assert gasesteMaximLexicografic1("Ana are mere si pere") != "mere"
    assert gasesteMaximLexicografic2("Ana are mere si pere") != "mere"


if __name__ == '__main__': 
    test()
    #Varianta 1
    sirInitial = input(">>Dati o propozitie: ")
    print(">>>>Varianta 1.")
    print(gasesteMaximLexicografic1(sirInitial))

    #Varianta 2
    print(">>>>Varianta 2.")
    print(gasesteMaximLexicografic2(sirInitial))
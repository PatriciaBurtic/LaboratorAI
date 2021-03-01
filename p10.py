def numaraUnu(linie):
    #Complexitate O(n)
    nr = 0
    for cifra in linie[::-1]:
        if cifra == 0:
            return nr
        else:
            nr = nr+1
    return nr

def citesteMatrice(cale):
    #Complexitate O(n^2)
    matrice=[]
    with open(cale,'r') as f:
        matrice = [[int(num) for num in line.split(',')] for line in f]
    return matrice

def identificaMaxUnu(matrice):
    #Complexitate O(n)
    i = 0
    indiceMax = 0
    max = 0
    for linie in matrice:
        numar = numaraUnu(linie)
        if numar > max:
            max = numar
            indiceMax = i
        i = i+1
    return indiceMax

def test():
    assert identificaMaxUnu(citesteMatrice('d:/UBB_info_sem_4/AI/LAB/Lab1/test.txt')) == 3

if __name__ == '__main__':
    test()
    matrice = citesteMatrice('d:/UBB_info_sem_4/AI/LAB/Lab1/input.txt')
    print(identificaMaxUnu(matrice))

    

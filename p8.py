def zecimalInBinar(n):
    #Complexitate O(log n)
    return bin(n).replace("0b", "") 

def convertesteTotInBinar(n):
    #Complexitate O(n)
    sir = []
    for numar in range(1,n+1):
        sir.append(zecimalInBinar(numar))
    return sir

def test():
    assert convertesteTotInBinar(4) == ['1', '10', '11', '100']
    assert convertesteTotInBinar(2) == ['1', '10']
    assert convertesteTotInBinar(3) == ['1', '10', '11']
    assert convertesteTotInBinar(3) != ['1', '10', '111']

if __name__ == '__main__':
    test()
    n = int(input(">>Dati un numar natural:"))
    print(convertesteTotInBinar(n))

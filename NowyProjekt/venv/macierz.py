macierz =[[0,0,1],[1,0,0],[0,1,0]]

for i in range(3):
    print("\n")
    for j in range(3):
        print(macierz[i][j],end=" ")



def dodawanie(x, y):
    suma= x + y
    return suma

def odejmowanie(x, y):
    roznica = x - y
    return roznica

def mnozenie(x, y):
    iloczyn = x * y
    return iloczyn

def dzielenie(x, y):
    iloraz = x/y
    return iloraz



print(dodawanie(4,5))
print(odejmowanie(9,5))
print(mnozenie(2,3))
print(dzielenie(9,3))
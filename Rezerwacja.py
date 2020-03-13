import Zapisodczyt
import Wyswietl
import Sala
import os

def book(lista,miejsce):
    it = 0
    zero = "0"
    temp = ''.join(lista)
    lista1 = temp.split(" ")
    while it != len(lista1) :
        if lista1[it] == miejsce:
            lista1[it] = 'x'
            return lista1
        it += 1
    print("To miejsce jest juz zajete ")
    print()
    return zero
def delbook(lista,miejsce):
    it = 0
    it2 = 0
    zero = "0"
    index = int(miejsce)
    temp = ''.join(lista)
    temp = temp.split(" ")
    lista1 = list(temp)
    lista1[index-1] = miejsce
    return lista1


#miejsce = Zapisodczyt.usunrez(1)
#miejsce = miejsce.split("-")
#lista1 = Zapisodczyt.odczyts("Sala A.txt", str(miejsce[3]))
#lista2 = delbook(lista1, str(miejsce[4]))
#temp = ''.join(lista2)
#print(miejsce[3],lista1,temp)
#print(delbook(['1 2 x 4 5 6 7 8 9 x 11'],"10"))

import sys
import Zapisodczyt


def odczyt2(sala,czas) :
    lista = Zapisodczyt.odczyts(sala,czas)
    slowo = lista[0]
    slowo = slowo.split(" ")
    wyraz = "  "
    for i in range(0,6):
        wyraz += slowo[i] + " "
    wyraz += "\n "
    for i in range(6,12):
        wyraz += slowo[i] +" "
    wyraz += "\n"
    for i in range(12, 18):
        wyraz += slowo[i] + " "
    return wyraz


#print(odczyt2("Sala D.txt",'14:00'))
import linecache
from shutil import copyfile


def odczyts(plik,temp):
    tab = []
    wiersz = " "
    index = 0
    while wiersz != "":
        wiersz = linecache.getline(plik, index + 1)
        if wiersz.startswith(str(temp)) == True:
            text = linecache.getline(plik, index + 2)
            tab.append(text[0:len(text) - 1])
            break
        index += 1
    return tab
def odczytf(plik) :
    text = open(plik).read()
    return text
def odczytrez(plik) :
    text = open(plik).read()
    return text
def zapisrez(nazwa,password,film,czas,miejsce):
    wiersz = " "
    index = 0
    text = open('Rezerwacje.txt').read()
    dane = open('help.txt', "w")
    x = 0
    while wiersz != "":
        wiersz = linecache.getline('Rezerwacje.txt', index + 1)
        temp = wiersz
        tab = temp.split("/")
        index += 1
        if tab[0] == nazwa:
            if tab[1] == password:
                if tab[2] == film:
                    if tab[3] == czas:
                        if miejsce == tab[4]:
                            continue
        dane.write(wiersz)
    dane.close()
    copyfile("help.txt","Rezerwacje.txt")
def zapis(plik,temp,lista):
    wiersz = " "
    index = 0
    dane = open(plik, "r+")
    x = 0
    while wiersz != "" :
        wiersz = linecache.getline(plik, index + 1)
        index += 1
        if wiersz.startswith(temp) == True:
            x = index + 1
        if index == x :
            dane.write(lista+'\n')
            continue
        dane.write(wiersz)
    dane.close()

def odczytgodz():
    i = 0
    tabhours = []
    text = open("Filmy.txt").read()
    temp = text.split("  ")
    length = len(temp)

    while i < length - 1:
        i += 1

        if i % 6 >= 3 or i % 6 == 0:
            tabhours.append(temp[i])

    return tabhours
def odczytfilmy():
    i = 0
    tabfilmy = []
    text = open("Filmy.txt").read()
    temp = text.split("  ")
    length = len(temp)

    while i < length - 1:
        i += 1
        if i % 6 == 2:
            tabfilmy.append(temp[i])

    return tabfilmy
def zapisrezerwacji(name,password,film,czas,miejsce):
    text = open("Rezerwacje.txt", 'a')   
    text.write(str(name) + "/"+str(password)+"/"+ str(film) + "/" + str(czas) + "/" + str(miejsce) + "/\n")
    text.close()

def odczytrezerwacji(name,password):
    wiersz = " "
    index = 0
    tablica = []
    text = open('Rezerwacje.txt').read()
    x = 0
    while wiersz != "":
        wiersz = linecache.getline('Rezerwacje.txt', index + 1)
        temp = wiersz
        tab = temp.split("/")
        index += 1
        if tab[0] == name:
            if tab[1] == password:
               tablica.append(temp)
    return tablica

def odczytrezerwacjinr(name,password):
    wiersz = " "
    index = 0
    tablica = []
    text = open('Rezerwacje.txt').read()
    x = 0
    while wiersz != "":
        wiersz = linecache.getline('Rezerwacje.txt', index + 1)
        temp = wiersz
        tab = temp.split("/")
        index += 1
        if tab[0] == name:
            if tab[1] == password:
               tablica.append(index)
    return tablica

def usunrez(nr):
    wiersz = " "
    index = 0
    text = open('Rezerwacje.txt').read()
    dane = open('help.txt', "w")
    x = ""
    while wiersz != "":
        wiersz = linecache.getline('Rezerwacje.txt', index + 1)
        temp = wiersz
        temp = temp.split("/")
        index += 1
        if str(nr) == str(index):
            x = temp[0]+"-"+temp[1]+"-"+temp[2]+"-"+temp[3]+"-"+temp[4]
            continue
        dane.write(wiersz)
    dane.close()
    copyfile("help.txt", "Rezerwacje.txt")
    return x
    
    
#zapisrez('Beniamin Kozyra','film1','10:00','2')
#print(odczyts("Sala A.txt",'12:00'))
#print(zapis("Sala "+"A"+".txt","10:00",'1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18'))
#print(odczyts("Sala A.txt",'10:00'))
#print(odczyt("Sala A.txt",'y'))
#print(odczytfilmy())
#print(odczytgodz())



import linecache
def Sala(film,czas):
    sala = ''
    index = 0
    i = 0
    wiersz = ' '
    while wiersz != "":
        wiersz = linecache.getline("Sala.txt", index + 1)
        sala = wiersz
        tab = sala.split(" ")
        if tab[0] == film:
            while i<len(tab) :
                if tab[i+1] == czas :
                    wyraz = tab[i+2]
                    return wyraz[0]
                else :
                    i = i+2
                    continue
        else :
            index += 1



#print(Sala("film1","11:00"))
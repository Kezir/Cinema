from tkinter import *
import Zapisodczyt
import Sala
import Wyswietl
import Rezerwacja

root = Tk()
root.title("Cinema")


def logowanie(name,password):
    menu()
def menu():
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    witamy = Label(root, text="Witamy w naszym kinie " + str(Name), width=30, height = 6,font = (15))
    rez = Button(root, text="Rezerwacja", width=30,command = rezerwacja,bg = "white")
    anulujrez = Button(root, text="Zobacz swoje rezerwacje", width=30,command = zobacz,bg = "white")
    wroc = Button(root, text="Wroc do logowania", width=30,command = start,bg = "white")
    witamy.grid(row=0, column=0)
    rez.grid(row = 1, column = 0)
    anulujrez.grid(row = 2,column = 0)
    wroc.grid(row = 3,column = 0)

def zobacz():
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    indexx = 0
    indexy = 1
    index = 0
    lista = ["przycisk1","przycisk2","przycisk3","przycisk4","przycisk5"]
    slowo = ""
    tab1 = Zapisodczyt.odczytrezerwacjinr(Name,Password)
    tab2 = Zapisodczyt.odczytrezerwacji(Name,Password)
    if len(tab2) == 0:
        list = root.grid_slaves()
        for l in list:
            l.destroy()
        brak = Label(root, text="Nie posiadasz zadnych rezerwacji ", width=30, height=6, font=(15))
        buttonbrak = Button(root, text="Wroc do Menu ",command = menu)
        brak.grid(row = 0, column = 0)
        buttonbrak.grid(row = 1, column = 0)
    else:
        Label4 = Label(root, text="Twoje rezerwacje: ",font = (12))
        Label4.grid(row = 0,column = 0)
        for i in range (0,len(tab2)):
            slowo = tab2[i]
            slowo = slowo.split("/")
            text = "Nazwa: "+slowo[2]+", Godzina: "+slowo[3]+", Miejsce: "+slowo[4]
            tab2[i]=Button(root, text=text,width = 60,bg = "white",command = lambda i=i : wlasciwosci(tab1[i]))
            tab2[i].grid(row = indexy,column = 0)
            indexy += 1
        label1 = Label(root,text="")
        label1.grid(row=8)
        button5 = Button(root, text="Wroc", width=30, command=menu)
        button5.grid(row=9, column=0)

def usun(nr):
    miejsce = Zapisodczyt.usunrez(nr)
    miejsce = miejsce.split("-")
    sala = "Sala " + Sala.Sala(miejsce[2], miejsce[3]) + ".txt"
    lista1 = Zapisodczyt.odczyts(sala, str(miejsce[3]))
    lista2 = Rezerwacja.delbook(lista1, str(miejsce[4]))
    temp = " "
    temp = temp.join(lista2)
    Zapisodczyt.zapis(sala,miejsce[3],temp)
    wyjscie("Pomyslnie usunales rezerwacje")

        
def wlasciwosci(nr):
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    label1 = Label(root,text = "Czy chcesz usunac swoja rezerwacje? ",height = 10,font = (12))
    label1.grid(row = 0,column = 1)
    tak = Button(root, text="Tak",width = 10,command =lambda: usun(nr))
    nie = Button(root, text ="Nie",width = 10,command = menu)
    tak.grid(row = 1,column = 2)
    nie.grid(row = 1,column = 0)

def rezerwacja():
    indexx = 0
    indexy = 0
    i = 0
    films = ["1","2","3","4"]
    button = ["button1","button2","button3","button4"]
    tabhours = [[]]
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    tabhours = Zapisodczyt.odczytgodz()
    tabfilmy = Zapisodczyt.odczytfilmy()

    for x in range(0,len(tabfilmy)):
        temp = button[x]
        temp = Button(root,text = tabfilmy[x],width = 30,bg = "white",font = 10,command =lambda x = x:video(films[x]))
        x = Label(root,text = tabhours[indexy:indexy+4],width = 30,font = 12)
        temp.grid(row = indexx,column = 0)
        x.grid(row = indexx+1, column = 0)
        indexx += 2
        indexy += 4
    bwroc = Button(root, text="Wroc do Menu",bg = "white",width = 15,command=wroc)
    bwroc.grid(row = 9,column = 0,rowspan = 3)
def wroc():
    rezerwacja()
def video(nr):
    indexx = 0
    indexy = 0
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    tabhours = Zapisodczyt.odczytgodz()
    tabfilms = Zapisodczyt.odczytfilmy()
    if nr == "1":
        nr = 1
        lista = tabhours[:4]
    elif nr == "2":
        nr = 2
        lista = tabhours[4:8]
    elif nr == "3":
        nr = 3
        lista = tabhours[8:12]
    elif nr == "4":
        nr = 4
        lista = tabhours[12:16]
    label1 = Label(root,text = "")
    global rez,film
    rez = Button(root,text="Rezerwuj",state = 'disabled',width = 15)
    rez.grid(row = 5,column =2,columnspan = 2)
    wroc = Button(root, text="Wroc",command = menu,width = 15)
    wroc.grid(row=5, column=0, columnspan=2)
    label1.grid(row = 3)
    przycisk = Label(root, text="", font=("Courier", 18))
    przycisk.grid(row=3, column=1, columnspan=2)
    film = tabfilms[nr-1]
    for i in range (0,len(lista)):
        tabhours[i] = Button(root, text=lista[i],width = 18,bg = "white",command =lambda i=i : czas(lista[i],przycisk))
        tabhours[i].grid(row = indexy,column = indexx)
        indexx += 1
        if indexx == 4:
            indexy += 1
            indexx = 0

def last(number):
    if number.isdigit() :
        number = int(number)
        if number <= 18:
            lista1 = Zapisodczyt.odczyts(sala, hour)
            lista2 = Rezerwacja.book(lista1, str(number))
            if lista2 != "0" :
                slowo = ' '.join(lista2)
                Zapisodczyt.zapis(sala, hour, slowo)
                Zapisodczyt.zapisrezerwacji(Name,Password,film,hour,number)
                wyjscie("Pomyslnie zarezerwowales miejsce")
def wyjscie(slowo):
    list = root.grid_slaves()
    for l in list:
        l.destroy()
    label2 = Label(root, text=slowo, font=(12))
    label2.grid(row=0, column=0, columnspan=3)
    label3 = Label(root, text="Czy chcesz wrocic do Menu ?",font = 10)
    label3.grid(row=1, column=1)
    label3 = Label(root, text="")
    label3.grid(row=2, column=1)
    button1 = Button(root, text="Wroc do Menu",command = menu,width = 15)
    button1.grid(row=3, column=0)
    button2 = Button(root, text="Wyjdz z programu",width = 15,command = drzwi)
    button2.grid(row=3, column=2)

def drzwi():
    sys.exit()

def czas(godz,przycisk):
    rez.config(state = 'normal',command = lambda: last(enumber.get()))
    global sala,hour
    hour = str(godz)
    video = film
    sala = "Sala "+str(Sala.Sala(video,hour))+".txt"
    text = Wyswietl.odczyt2(sala,hour)
    przycisk.config(text = text)
    enumber = Entry(root, width=35, borderwidth=5)
    enumber.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    enumber.insert(0, "Wpisz numer ktory cie interesuje")



def getvalue(name,password):
    global Name,Password
    Name = name
    Password = password
    if name == "" or password == "":
        start()
    else:
        logowanie(name,password)

def start():

    list = root.grid_slaves()
    for l in list:
        l.destroy()
    labelname = Label(root, text ="Nick ").grid(row = 0,column= 0, stick = E)
    labelpassword = Label(root, text ="Password ").grid(row = 1,column= 0, stick = E)
    ename = Entry(root, width=35, borderwidth=5)
    ename.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
    epass = Entry(root, width=35, borderwidth=5)
    epass.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    button_logowanie = Button(root, text="Zaloguj", padx=40, pady=10, command=lambda : getvalue(ename.get(),epass.get()))
    button_logowanie.grid(row = 2,column = 1)

start()
root.mainloop()



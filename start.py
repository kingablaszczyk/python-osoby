import csv
osoby= []

def wczytaj_osoby():
    try:
        plik=open('osoby.csv', 'r')
        csv_reader= csv.reader(plik)
        for row in csv_reader:
            osoba = {'id':row[0], 'imie':row[1], 'haslo':row[2]}
            osoby.append(osoba)
    except FileNotFoundError:
        plik = open('osoby.csv' , 'r')
        plik.close()

wczytaj_osoby()
czy_lista = input('Czy chcesz wyswietlic liste? (T/N)')

if czy_lista == 'T' or czy_lista == 't':

    print(osoby)
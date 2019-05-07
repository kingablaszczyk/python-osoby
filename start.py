import csv
import string
import random

osoby= []

def wczytaj_osoby():
    try:
        plik=open('osoby.csv', 'r')
        csv_reader= csv.reader(plik)
        for row in csv_reader:
            osoba = {'id' : int(row[0]), 'imie' : row[1], 'haslo' : row[2]}
            osoby.append(osoba)
    except FileNotFoundError:
        plik = open('osoby.csv' , 'w')
        plik.close()

def wygeneruj_haslo():
    haslo =''
    chars = string.ascii_letters + string.digits
    for char in range (10) :
        haslo += random.choice(chars)
    return haslo

def dodaj_osobe():
    imie = input('Podaj imię: ')
    plik = open('osoby.csv', 'a')
    csv_writer = csv.writer(plik, delimiter=',') #delimiter - rozgraniczenie rekordow
    csv_writer.writerow([len(osoby),imie,wygeneruj_haslo()])
    print('dodałes osobę')

czy_lista = input('Czy chcesz wyswietlic liste? (T/N)')

if czy_lista == 'T' or czy_lista == 't':
    print(osoby)


czy_dodac = input('Czy chcesz dodać nową osobę? (T/N)')

if czy_dodac == 'T' or czy_dodac == 't':
   dodaj_osobe()


from inspect import cleandoc
import sys

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#          print(a, end=' ')
#          a, b = b, a+b
#          print()
# fib(8)
#
# fruits = ['Banana', 'Apple', 'Lime']
# loud_fruits = [fruit.upper() for fruit in fruits]
# print(f'loud_fruits is',loud_fruits)
#
# for x,element in enumerate(fruits, start=1):
#     print(x, element)
#
#
# # List and the enumerate function
# list(enumerate(fruits))
# # [(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]

# x = 0
# lista_liczb = []
# i = 0
# while x <= 4:
#     num = int(input('podaj liczbe: '))
#     i += num
#     print(i)
#     lista_liczb.append(i)
#     x += 1
#
# print(lista_liczb)

#od 0 do 200  podzielne przez 5 anie podzielne przez 7
# for i in range(201):
#     if i % 5 == 0 and i % 7 != 0:
#         print(f'liczba {i} jest podzielna przez 5 ale nie przez 7')

# names= ['michal', 'puszka', 'jeden', 'test', 'tester']
#
# name = input()
#
# if name=='michal':
#     print('masz dostep')
# else:
#     print('brak dostepu')

# ratings1 = {
#             "Arkadiusz": (2,1,2,3,2,3),
#             "Agnieszka": (4,2,1,3,4),
#             }
# #
# #
# for k,v in ratings1.items():
#     print(k)
#     print(v)
#     print()
#
# for key in ratings1:
#     print(f'{key} oceny {ratings1[key]}')


# people2 = [
#          {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
#          {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
#          {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
#           ]
#
# for v in people2:
#     for k in v:
#         print(f'{k} : {v[k]}')
people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
         }
#
# for key in people:
#     print(f'ID: {key}')
#     for seckey in people[key]:
#         print(f'{seckey}:{people[key][seckey]}')

# for k,v in people.items():
#     print(f'ID:{k}')
#     for k2 in v:
#         print(f'{k2}: {v[k2]}')

# cleandoc('''
# program do dodawania nowych definicji
# szukac istniejacych definicji
# usuwac wybrane definicje
# ''')
#
# program = {}
#
# # print('1: Dodaj definicje')
# # print('2: znajdz definicje')
# # print('3: usun definicje')
# # print('4: zakoncz- wyjscie  zprogramu')
# #
# # wybor_usera = int(input('co cchesz zrobic?? wcisnij liczbe od 1 do 4'))
# while True:
#         print('1: Dodaj definicje')
#         print('2: znajdz definicje')
#         print('3: usun definicje')
#         print('4: zakoncz- wyjscie  zprogramu')
#
#         wybor_usera = int(input('co cchesz zrobic?? wcisnij liczbe od 1 do 4'))
#         if wybor_usera == 1:
#                 definicja = input("Podaj definicje ktora chcesz dodac do slownika")
#                 wyjasnienie = input('wyjasnij definicje ktora chcesz dodac do slownika')
#                 program.update({definicja:wyjasnienie})
#                 print(program)
#         elif wybor_usera == 2:
#                 szukany_klucz = input('Wybierz definicje ktora chcesz znalesc')
#                 if szukany_klucz in program:
#                         print(f'Szukana definicja to: {program[szukany_klucz]}')
#                 else:
#                         print(f'nie znaleziono takiej definicji {szukany_klucz}')
#         elif wybor_usera == 3:
#                 definicja_do_usuniecia = input('Wybierz definicje do usuniecia z programu')
#                 program.pop(definicja_do_usuniecia)
#                 print(f'Usunales: {definicja_do_usuniecia}')
#         elif wybor_usera == 4:
#                 print('Wychodzimy z propgramu')
#                 sys.exit()
#         else:
#                 print('podales zle dane - sproboj jeszcze raz')

# liczby = [1, 2, 3, 4, 5, 6]
#
#
# potegi_dwojki = [e**2
#                  for e in liczby
#                  ]
# print(potegi_dwojki)
#
# liczbyparzyste = [e
#                   for e in liczby
#                   if (e % 2 == 0)
#                   ]
# print(liczbyparzyste)

# evennumbers = [num for num in range(400) if (num % 2==0)]
# print(f'{evennumbers}')
#
# evengennumbers = (num for num in range(400) if (num % 2==0))
# print(evengennumbers)
# print(sum(evengennumbers))
# print(sys.getsizeof(evennumbers))
# print(sys.getsizeof(evengennumbers))
# for item in evengennumbers:
#     print(item)

# names = {"Arkadiusz", "Wioletta", "Karol", "Bart??omiej", "Jakub", "Ania"}
#
# nameslenght = {
#     name: len(name)
#     for name in names
#     if name.startswith('A')
# }
#
# print(nameslenght)
#
# celsius = {'t1':-20,'t2':-15, 't3':0, 't4':12, 't5':24}
#
# fahrenheit = {
#     k : temp * 1.8 + 32
#     for k,temp in celsius.items()
#     if temp > -5
#     if temp < 20
# }
#
# print(fahrenheit)

# names = {"arkadiusz", "Wioletta", "karol", "bart??omiej", "Jakub", "Ania"}
#
# names_ = {
#     name.capitalize()
#     for name in names
# }
#
# print(names_)

# cleandoc(
#     """"
# liczby od 100 do 470 ktore sa podzielne przez 7 ale nie sa podzielne przez 5
# """""
# )
#
# numsgenerator = [
#     num
#     for num in range(100, 471)
#     if num % 7 == 0
#     if num % 5 != 0
# ]
# #
# # for num in numsgenerator:
# #     print(num)
#
# print(numsgenerator)
import math
cleandoc("""
Stw??rz menu, z kt??rego u??ytkownik, mo??e wybra?? opcje, aby policzy?? powierzchnie figur:
1) prostok??ta
2) kwadratu
3) tr??jk??ta
4) trapezu
5) ko??a
Pami??taj, by skorzysta?? z funkcji.
""")

# def pole_prostok??ta(a,b):
#     return a * b
# def pole_kwadratu(a):
#     return a**2
# def pole_trojkata(a,h):
#     return 0.5* a * h
# def pole_kola(r):
#     return 3.14 * r ** 2
# def pole_trapezu(a,b,h):
#     return (0.5 * (a+b)) * h
#
#
# x= pole_trapezu(2,5,2)
# print(x)
# a = pole_kola(3)
# print(a)
# b =pole_trojkata(4,4)
# print(b)


"""
Napisz funkcj??,
kt??ra jako argument przyjmuje list?? liczb 
i zwraca sum?? wszystkich liczb dodatnich na li??cie. 
Funkcja powinna ignorowa?? wszelkie liczby ujemne lub zera na li??cie.
"""

# def suma_liczb(numbers):
#     return sum([num for num in numbers if num > 0])
#
# numbers = [1,-5,2,4,-10,20]
#
# x = suma_liczb(numbers)
# print(x)
import random
# x = 0
# while x < 100:
#     a = random.randint(0,100)
#     print(a)
#     x +=1

# def czy_uderzysz_przeciwnika(percent_probably_to_hit):
#     weapon_hit = random.randint(0,100)
#     if weapon_hit <= percent_probably_to_hit:
#         return 'hit'
#     else:
#         return 'not hit'
#
# # x = czy_uderzysz_przeciwnika(50)
# # print(x)
# listhit = []
# a=0
# while a < 100:
#     listhit.append(czy_uderzysz_przeciwnika(50))
#     a += 1
#
# # print(listhit)
# # print(listhit.count('hit'))
# # print(listhit.count('not hit'))
# from collections import Counter
#
# dicthit = Counter(listhit)
# print(dicthit)

# movieList = ["Tytu??1", "Tytu??2", "Tytu??3", "Tytu??4"]
# # print(random.choice(movieList))
# event = ['wygrana', 'smierc', 'przegrana', 'utratas zlota' , 'losowa rzecz']
# nagroda = ['zielona', 'pomaranczowa', 'purpurowa', 'legendarna']
# from collections import Counter
# print(Counter(random.choices(nagroda,[80,15,4,1], k=100)))
#
#
# cardList = [ "9", "9", "9", "9",
#              "10", "10", "10", "10",
#              "Jack", "Jack", "Jack", "Jack",
#              "King", "King", "King", "King",
#              "Queen", "Queen", "Queen", "Queen"
#              "Ace", "Ace", "Ace", "Ace",
#              "Joker", "Joker"
#            ]
#
# random.shuffle(cardList)
# print(cardList)

"""Napisz funkcj??, kt??ra zasymuluje jak dzia??a 
Lotto tzn. wybierze 6 unikalnych liczb z 49."""
# def lotto():
#     print(random.sample(range(1,50), 6))
#
# a = lotto()

# from enum import Enum
# event = Enum('Event', ['Skrzynia', 'Pusty'])
#
# eventDict = {
#             event.Skrzynia : 0.6,
#             event.Pusty : 0.4,
# }
# evenList = list(eventDict.keys())
# evenList_probability = list(eventDict.values())
#
# kolory = Enum('Kolory',{'Green': 'zielony',
#                         'Orange' : 'pomaranczowy',
#                         'Purple': 'fioletowy',
#                         'Gold' : 'zloty'
#                         }
#               )
#
# probability_kolory = {
#     kolory.Green : 0.60,
#     kolory.Orange : 0.20,
#     kolory.Purple : 0.15,
#     kolory.Gold : 0.05
# }
# coloursList = list(probability_kolory.keys())
# coloursList_probability = list(probability_kolory.values())
#
# nagrodazaskrzynke = {
#             coloursList[reward]: (reward+1) * (reward+1) * 1000
#             for reward in range(len(coloursList))
# }
#
# gameLenght = 5
#
# sumanagrodgracza = 0
# while gameLenght > 0:
#     gamer_response = input('Do you wanna move forward?')
#     if gamer_response == 'yes':
#         print('ok sprawdzmy co masz')
#         drawnEvent = random.choices(evenList,evenList_probability)[0]
#         if (drawnEvent == event.Skrzynia):
#             print('wylosowales skrzynke')
#             drawnkolor = random.choices(coloursList,coloursList_probability)[0]
#             print(drawnkolor.value)
#             nagrodagracza = nagrodazaskrzynke[drawnkolor]
#             print(f'w tej rundzie zdobyles {nagrodagracza}')
#             sumanagrodgracza = sumanagrodgracza+nagrodagracza
#         elif drawnEvent == event.Pusty:
#             print('wylosowales nic')
#     else:
#         print('mozesz chodzic tylko do prostu')
#         continue
#
#     gameLenght -= 1
#
# print(f'zdobyles {sumanagrodgracza} punktow')

"""

JSON

"""
# import json
#
# film = {
#     'title': 'Ale ja nie b??d?? tego robil!',
#     'release_year' : 1969,
#     'won_oscar' : True,
#     'actors' : ('Micha??','Marlena'),
#     'budget' : None,
#     'credits' : {
#         'director' : 'Micha??',
#         'writer' : 'Marlena',
#         'animator' : 'marcin'
#     }
# }
#
# x = json.dumps(film, ensure_ascii=False, indent=4,)
#
# with open('przyklad.json', 'w', encoding='UTF-8') as file:
#     json.dump(film, file, ensure_ascii=False, indent=4)
# print(x)
#
# with open('file.json', encoding='UTF-8') as file:
#     x = json.load(file)
#
# # print(json.dumps(x,indent=4, sort_keys=True))
#
# import pprint
# pprint.pprint(x, indent=4)

# with open('oceany.txt', 'a', encoding="UTF-8") as file:
#     file.write('\ntest')
#     print(file.tell())

# x = []
# with open('imionanazwiska.txt', 'r',encoding="UTF-8" ) as file:
#         for line in file:
#                 x.append(tuple(line.replace('\n', "").split(' ')))
# print(x)
#
# with open('imiona.txt', 'w',encoding="UTF-8" ) as file:
#         for item in x:
#                 file.write(item[0] + '\n')
#
# with open('nazwiska.txt', 'w',encoding="UTF-8" ) as file:
#         for item in x:
#                 try:
#                         file.write(item[1] + '\n')
#                 except IndexError:
#                         file.write('\n')

cleandoc("""Stw??rz funkcj??, kt??ra obs??uguje otwieranie pliku do wczytywania danych.
Zapytaj si?? u??ytkownika o nazw?? pliku, kt??ry chce otworzy?? do wczytania.
Je??li plik nie istnieje wypisz mu odpowiedni komunikat.
Je??li plik istnieje wczytaj ca???? jego zawarto???? i zwr???? jako wynik funkcji.
Podpowied??: skorzystaj z wiedzy dotycz??cej obs??ugi wyj??tk??w z poprzedniej lekcji:
except FileNotFoundError:""")

# def open_file_to_read_data(path):
#         try:
#                 with open(path, 'r',encoding="UTF-8") as file:
#                         print(file.read())
#         except FileNotFoundError:
#                 print('Nie znaleziono takiego pliku')
#
# ask_about_name_file = input('Podaj nazwe pliku jaka cchesz otworzyc: ')
#
# file_name = open_file_to_read_data(ask_about_name_file)

cleandoc("""
1) Napisz kod, kt??ry sprawdzi, jak cz??sto s??owo "kot" wyst??puje w pliku "tekst.txt".
Dane wej??ciowe:
??cie??ka do pliku: "tekst.txt"
S??owo do wyszukania: "kot"
Dane wyj??ciowe:
Liczba wyst??pie?? s??owa "kot" w pliku "tekst.txt":
Przyk??ad:
Je??li w pliku "tekst.txt" znajduje si?? tekst "Kot jest bardzo fajnym zwierz??ciem", to kod powinien wy??wietli?? "S??owo 'kot' wyst??pi??o 1 razy w pliku 'tekst.txt'."
Wskaz??wki:
Otw??rz plik w trybie odczytu i za pomoc?? metody count zlicz wyst??pienia s??owa w ca??ym pliku.
Wy??wietl wynik za pomoc?? instrukcji print.
2) Pami??taj o obs??udze wyj??tk??w!
FileNotFoundError wyst??puje, gdy plik o podanej ??cie??ce nie zostanie znaleziony.
PermissionError wyst??puje, gdy brak jest uprawnie?? do odczytu pliku.
3) Gdy wypiszesz dane skorzystaj z formatted stringa
Przyk??ad:
imie = "Jan"
wiek = 30
print(f"Cze????, nazywam si?? {imie} i mam {wiek} lat.")  # wy??wietli "Cze????, nazywam si?? Jan i mam 30 lat."
"f" na pocz??tku ci??gu znak??w oznacza, ??e jest to tzw. f-string (ang. formatted string).
F-string to nowa wersja ci??g??w znak??w w Pythonie, kt??ra pozwala na szybkie i ??atwe formatowanie ci??g??w znak??w za pomoc?? zmiennych i wyra??e??.
F-string pozwala na oszcz??dzenie czasu i linii kodu, poniewa?? nie trzeba ju?? u??ywa?? operatora "+" do po????czenia ci??g??w znak??w ze zmiennymi.
Uwaga: f-string dost??pny jest od Python 3.6. Je??li u??ywasz starszej wersji Pythona, mo??esz u??y?? operatora "+" do formatowania ci??g??w znak??w.
""")

file = 'text.txt'
word = 'kot'
try:
        with open(file, 'r', encoding="UTF-8") as file:

                tekst = file.read()
                wystapienia = tekst.count(word)

        print(f'Slowo {word} wystepuje tyle razy: {wystapienia}')
except FileNotFoundError:
        print(f'Nie ma takiego pliku o nazwie {file}')
except PermissionError:
        print(f'brak jest uprawnie?? do odczytu pliku {file}')

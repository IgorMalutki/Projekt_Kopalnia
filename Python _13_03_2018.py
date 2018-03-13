# Napisy

zdanie = 'Janek ma kota i kot ma Ale'

# Adresowanie po indeksie
print(zdanie[10])

# Adresowanie od indeksu do końca

print(zdanie[10:])

# Adresowanie od początku do indeksu

print(zdanie[:10])

#  Adresowanie zakresu indeksów

print(zdanie[2:5], len(zdanie[2:5]))

# zmiana zawartości

print(zdanie.replace(zdanie[10], 'p'))
print(zdanie)

# skracanie
'''zdanieSkrot = zdanie[0:10]
print(zdanieSkrot)

zdanie = zdanie[0:11]
print(zdanie)
'''''

# dzielenie napisu
print(zdanie.split(' '))
print(zdanie)

# Listy

L = [[1, 2, 3], ['a', 'b', 'c', 'd'], [['p', 'q'], 1]]

print(L[0][0])
print(L[2][0][1])
print(len(L[0]))

# dodawanie do listy
L.append('koniec')
print(L)

L.append(zdanie.split(' '))
print(L)

# zamiana elementu listy

L[4][4] = 'pies'
print(L)

# z 4 elementu drukuje co drugie słowo

print(L[4][0::2])

# usuwanie elementu listy
# pop  usuwa i zwraca co usunął
# remove - usuwa i koniec

'''L.remove(L[3])
print(L)

L123 = L.pop(0)
print(L123)
print(L)
'''

# Sprawdzanie zawartości list

print('koniec' in L)
print(['Ale'] in L)
print(L)

# Listy jako typ zmienny


txt1 = 'Do konwersji'
Ltxt = list(txt1[2:8])
print(Ltxt, type(Ltxt))

Ltxt.reverse()
print(Ltxt)

# zadanie rekrutacyjne  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

txt1 = 'koniec'
txt2 = list(txt1)
txt3 = list(txt1)
txt2.reverse()
print(txt2)
print(txt3)
print(txt2 == txt3)


#P39

liczby = []
imiona = []
ListList = [liczby, imiona]
liczby.append(1)
liczby.append(2)
liczby.append(3)
print(liczby)
imiona.append('Adam')
imiona.append('Ewa')
print(imiona)
ListList[0].append(1)
ListList[0].append(2)
ListList[0].append(3)
ListList[1].append('Adam')
ListList[1].append('Ewa')
print(ListList)


#P40

imie =  ListList[1][1]
print(imie)

#p41

lista = ['chleb','bulka', 'maka', 'cukier','sol']
print(lista[0],lista[len(lista)-1])
print(lista[::len(lista)-1])
print(lista[-1])  # określenie ostatniego elementu listy

#krotki

k = ([1,2],1,[2,3])
#k[1]=2  NIE WOLNO  !!!!!!!!!!!!!!
k[0][0]=2 # WOLNO !!!!!!!!!!!!!!!!!
print(k)


#P42

p = 'Witaj na kursie Python'
slowa = tuple(p.split(' '))
print(slowa)


#P43

data = ('dzien','miesiac','rok')
nazwy = (['A','B','C'],('2017-01-01','2018-01-01','2019-01-01'))
print('Produkt' , nazwy[0][0],'data waznosci',nazwy[1][0])
print('Produkt' , nazwy[0][1],'data waznosci',nazwy[1][1])
print('Produkt' , nazwy[0][2],'data waznosci',nazwy[1][2])

# Słowniki

kolory = {'red':1111, 'blue':2222 , 'green':3333}
print("Klucze :",kolory.keys())
print('Wartości :',kolory.values())
print('green' in kolory.keys())
# dodawanie

kolory['yellow'] = 4444
print(kolory)

#modyfikacja
kolory['red'] = 5555
print(kolory)

#usuwanie
kolory.pop('red')
print(kolory)

print(2222 in kolory.values())

'''#p44
key = input('Podaj słownie liczbę z zakresu 1-5:')
liczby = {'jeden':1,'dwa':2, 'trzy':3, 'cztery':4,'pięć':5}
print('Twoja liczba to :',liczby[key] )
'''

#P45
'''
key =  int(input('Podaj liczbą całkowitą :'))
rzymskie = {1:'I',2:'II',3:'III',4:'IV',5:'V'}
print('Cyfra rzymska :',rzymskie[key])
'''

'''#P48
kod = input('Co kupujesz ? :')
szt = int(input('Ile szt ? :'))
prod = {'k1':['nazwa1',10.],'k2':['nazwa2',5.2],'k3':['nazwa3',3.1]}
print('Zamówienie: ', prod[kod][0], szt , prod[kod][1], szt*prod[kod][1]*1.23)
'''
A = set([1,2,3,4,5])
B = set ([1, 2, 'Ala'])

print(len(A),len(B))
print(3 in A)
print(A.issuperset(B),A.issubset(B))

#Opracje na zbiorach
print(A|B)
print(A&B)
print(B-A)
print(A^B)


# ZADANIE REKRUTACYJNE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#niepowtarzające się elementy w 2 listach

lista = set(['chleb','bulka', 'maka', 'cukier','sol'])
lista1 = set (['chleb', 'maka','pieprz'])
lista3 = list(lista^lista1)
print(lista3)

#P49
from random import randint , sample
lista = range(1,50)
res = sample(lista,6)
print(sorted(res))


#P50


print(list(range(2,100,2)))
print(list(range(-100,-2,2)))


#p51
x = list(range(1,21,2))
y = list(range(1,11))
wsp = (x,y)
print(wsp)



# ZADANIE DOMOWE  !!!!!!!!!!!!!!!!!!!!!!!!!!!! P52


# INSTRUKCJE WARUNKOWE


#P55




L = [1,2,3,4,5,6]

if (L[0]>0 and L[1]>0):
    print('++')
elif (L[0]<0 and L[1]>0):
    print('-+')
elif (L[0]>0 and L[1]<0):
    print('-+')
else:
    print('--')

'''
pattern =  [1,2,3,4,5,6]
score = []
ocena = input('Podaj ocenę : ')
if (ocena.isdigit()):
    ocena = int(ocena)
    if(ocena in pattern):
        score.append(ocena)
        print('OK')
    else:
        print('Zła wartość')
else:
    print('Krzaki')
'''

'''#Wyrażenie trójargumentowe
login = input('Podaj login:')
haslo = input('Podaj haslo:')



print('Witam bossa') if(login=='admin' and haslo=='admin') else print('Nie jesteś bossem')

'''


#P53

if(0):
    print('OK')
else:
    print('NOT OK')


#P54


x = 5
print('OK') if (x >=0 and x<=9) else print('Out of Range')


#P56

#liczba = int(input('Podaj liczbę calkowitą :'))
#print('parzysta') if (int(input('Podaj liczbę calkowitą :'))%2==0) else print('Nieparzysta')

#Pętle
'''
L = []
i = 1
while(i<=5):
    L.append(input('Podaj element'+str(i)+'n-ty listy'))
    i+=1
    print(L)
print(L)

'''

lista = list(range(1,49))
i=0
while(i<len(lista)):
    if(lista[i] % 3 == 0):
        print(lista[i],end=' ')
    i+=1


#losowanie LOTTO

los = set()
i = 0
while(len(los)<6):
    los.add(randint(1,49))
print('Wynik:', sorted(los))

lista = list(range(1,49))
for i in lista:
    print(i,end=' ')

for i,v in enumerate(lista):
    print(i,v, end='\n')
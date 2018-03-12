# komentarz jednowierszowy
''' komentarz blokowy
komentarz blokowy '''

print('qwerqwerqwerqwreqwer')
zmiennaJeden = 12
zmiennaFloat = 5.25
zmienna6 = 'abc'
zmiennaNapis = "TXT"
myBool = True
myBool2 = False
nic = None

print(zmiennaJeden, zmiennaFloat, zmienna6, zmiennaNapis, myBool, myBool2, end='|')
print(zmiennaJeden, zmiennaFloat, zmienna6, zmiennaNapis, myBool, myBool2, sep='@')

nowa = zmiennaJeden + 15
print('Wynik :', nowa)
print(zmiennaNapis + zmiennaNapis + str(zmiennaJeden))
print(type(zmiennaJeden), type(zmiennaNapis), type(myBool), type(zmiennaFloat), type(nic))
''' uwaga na wartości zmiennych przy przypisywaniu wartości , przypisujesz aktualną 
wartość a nie odwolanie do aktualne wartości'''
a = 1
b = a
a = 2
print(a, b)  # wynik 2,1
b = a
print(a, b)  # wynik 2,2

''' usuwanie zmiennej
c = 1
del (c)
print(c)'''

print('Modulo', 5 % 2)
# P1
a = 1
b = 2.4
c = 'w1'
print(a, b, c, sep='\t')

# P2
a = 2.1
b = 'abc '
c = 0
print("Nowe wartości", a, b, c)

# P3
b = c
a = 13
print("Nowe wartości", a, b, c)

'''P4

del(a,c)
print(a,c)
'''

# P5
imie = 'Irek'
nazwisko = 'Zadlo'
rok_urodzenia = '1974-07-03'
stanowisko = 'kierownik'
płaca = 10000.00
print(imie, nazwisko, rok_urodzenia, stanowisko, płaca, round(płaca, 2),
      round(płaca * 1.23, 2))  # zaokragla matematycznie
print('%s %s %s %s %7.2f %7.2f' % (
    imie, nazwisko, rok_urodzenia, stanowisko, płaca, płaca * 1.23,))  # uzupełnia miejsca zerami

# p6
from math import pi as pi_import

r = 3
print(pi_import * r * r)
print(pi_import * pow(r, 2))
print(round(pi_import * (r ** 2), 2))

'''#P7

for = 1
print(for)
'''

print(1e+2)
print(3 // 2)

p = 10.5 * 2
print(p, type(p))

x = 3 / 2
print(type(x))
print(round(-1.6))
print(int(-1.2 + 0.5))

# P8

print(type(imie), type(nazwisko), type(rok_urodzenia), type(stanowisko), type(płaca))

# p10

kwota = 1000

print(round(kwota / 1.03, 2), round(kwota / 1.07, 2), round(kwota / 1.23, 2))

# P11

cena_chleba = 1.99
cena_mleka = 2.5
cena_kg_cukierkow = 12.99

print('koszt zakupów :', (2 * cena_chleba) + (0.5 * cena_chleba) + (0.3 * cena_kg_cukierkow))

# p12

print((2 + 5j) + (4 + 6j), type((2 + 5j) + (4 + 6j)))
print(4 - (4 + 6j))

# p13-14

x = 100
y = 100
print('octal', oct(x))
print('hex', hex(y))

print(bool('abc'), bool(12), bool(0), bool(''), bool(None))

print('"""\m')  # \ i coś  tam musi być

print('Napis wiele\n' * 20)

# P16

print(bool(7), 4 > 3, 2 == 3, 2 != 3)

# 19

liczba = '5'

print(type(int(liczba) * 2))

'''liczba_in = int(input('Podaj liczbe całkowitą: '))
print(liczba_in,type(liczba_in))'''

# P24
'''
liczba_in = (input('Podaj dlugość odcinka: '))
print('Pole kwadratu o boku:',liczba_in,'wynosi :',round(liczba_in**2, 2))
print('Obwód trójkąta o boku: ',liczba_in,'wynosi :',round(liczba_in*3,2))
print('Pole koła o promieniu :',liczba_in,'wynosi :',round(pi_import*liczba_in ** 2,2))'''

# P26
p = False
q = True
print(not (p and q) == (not p or not q))

# P27

a = True
b = True
c = False

b1 = (not a and not b and not c)
b2 = (not a and not b and c)
b3 = (not a and b and not c)
b4 = (a and not b and not c)
print(b1 or b2 or b3 or b4)

print('ala' > 'ALA')

# 28


x = -17
print(x ** (1 / 2))

# P29

z = 17 % 7
z *= z + 3;
z = z**2 + 3*z
print(z)


#30

print ((str(1.2e+3+34.5)+";")*19 +str(1.2e+3+34.5))


#32

'''napis1 = input('1: ')
napis2 = input('2: ')
print('rowne' and napis1==napis2)
print('napis1 jest wiekszy' and napis1>napis2)

if(napis1 == napis2):
    print('Równe')
elif(napis1>napis2):
    print('1 wiekszy')
else:
    print('2 wiekszy')
'''

#P35

'''imie =  input('Podaj swoje imie ')
if ((imie[len(imie)-1].upper()) == 'A'):
    print('Dzień Dobry Pani')
else:
    print('Dzień Dobry Panu')
'''

#P38

SPK = float(input('Ile masz kasy ?:'))
P = float(input ('Wiela masz procentów ?:'))
N = int(input('Ile lat ? :'))

print ('Będziesz miał :',round(SPK*((1+P/100)**N),2))
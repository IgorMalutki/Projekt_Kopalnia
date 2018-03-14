#P57
Prod = {'k1': ['nazwa1', 10., 10], 'k2': ['nazwa2', 12.5, 5], 'k3': ['nazwa3', 33.1, 1]}
Zam = []
while(True):
    kod = input('podaj kod produktu: Q-wyjœcie')
    if(kod.upper() == 'Q'):
        break
    elif(kod in Prod.keys()):
        ilosc = int(input('podaj iloœæ produktu:'))
        if(ilosc <= Prod[kod][2]):
            print('Zamówiono produkt')
            Prod[kod][2] -= ilosc
            Zam.append([Prod[kod][0], ilosc*Prod[kod][1]])
        else:
            print('Za du¿o!!! Mamy braki na magazynie')
    else:
        print('Nie ma takiego produktu!')
DoZaplaty = 0
print('PARAGON')
for cena in Zam:
    print('%10s %6.2f z³' % (cena[0],cena[1]))
    DoZaplaty += cena[1]
print('%6.2f' % (DoZaplaty))
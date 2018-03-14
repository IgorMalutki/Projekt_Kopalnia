# potęgowanie
'''
podstawa = 5
wykładnik = 4
wynik = 1
i=1

while i<= wykładnik:
    wynik *= podstawa
    i+=1
    print(wynik)
print(wynik)


# ciąg geometryczny

a_0 = 3
q = 2
n = 5
i = 0
suma = 0

while n>0:
    suma+=a_0*(q**(n-1))
    n-=1
    print(suma)
print(suma)
'''


# formatowanie wyjścia


for x in range(5,100,15):
    print("%4i%6i%8i" % (x,x**2,x**3))

imiona = ['Ala' , 'Ola' , 'Aleksandra']


for i,imie in enumerate(imiona):
    print('%3i | %-15s' % (i+1,imie))

pomiary = [1.34,-2.34,3.44,2.12345]

for i, pomiar in enumerate(pomiary):
    print('%3i | %+-7.1f |' % (i+1, pomiar))


# BREAK

szukane = 15
flaga = False
L= list(range(1,100,2))
for elem in L:
    if(elem==szukane):
        flaga = True
        break
if flaga:
    print('Znaleziono')
else:
    print('Nie znaleziono')
'''# MENU - petla
while(True):
    decision = input('Co chcesz zrobić ?: 1-?, 2-?, q-wyjście')
    if decision.upper()=='Q':
        print('OUT')
        break
'''

#P57
prod = {'k1':['nazwa1',10.,10],'k2':['nazwa2',5.2,5],'k3':['nazwa3',3.1,1]}
zam = []
'''
while(True):
    kod = input('Co kupujesz ? :')
    if(kod in prod.keys()):
        szt = int(input('Ile szt ? :'))
        if szt <= prod[kod][2]:
            prod[kod][2]-szt
            print('Zamówienie: kod produktu: ',kod,',nazwa produktu: ',prod[kod][0],'\n,ilośc zamówiona: ',szt,
            ',cena produktu: ',prod[kod][2])
        else:
            print('Maks ilość to: ',prod[kod][2])
    else:
        print('Brak')

'''
#P60
'''
dana = input('Podaj ciag cyfr :')
cyfry_słownie = {1:'jeden', 2:'dwa', 3:'trzy'}
result=''
for znak in dana:
    if(znak.isdigit()):
        result += cyfry_słownie[int(znak)]
print(result)
'''

#P66

tab = [1,2,3,4,5,6,7,8,9]
n=1
while (n<=9):
    print('| %03i | %03i | %03i |'% (n,n**2, n**3))
    n+=1


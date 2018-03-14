# FUNKCJE

from random import randint

def lotto():
    Lotto = set()
    while (len(Lotto) < 6):
        Lotto.add(randint(1, 49))
    return Lotto

print(lotto())
'''
def logowanie(login, imie, nazwisko,password='****'):
    print(login, password, imie, nazwisko)

def logowanie1(login, imie, nazwisko,password='****'):
    return('%10s  %10s $10s %10s ' % (login, password, imie, nazwisko))

logowanie(login='rt',password='tr',imie='we',nazwisko='qw')

#P69
def silnia (n):
    try:
        n = int(n)
        if(n>0):
            wynik = 1
            while(n>0):
                wynik*=n
                n-=1
            return wynik
        else:
            return 'ERROR - ujemny argument funkcji'
    except:
        wynik = -1
        return 'ERROR'

print(silnia(input('Ile silnia?')))
'''

#P70 Fibonacciego

def fib (n):
    if(n==1 or n==2):
        return n,1
    elif(n<=0):
        return 'ERROR'
    else:
        F = [1,1]
        i=2
        suma = 0
        while(i<n):
            F.append(F[i-1]+F[i-2])
            i+=1
        for elem in F:
            suma+=elem

        return suma,F[len(F)-1]

print(fib(50))


#P71

def zdanie (wej,n):
    wej = wej.split(' ')
    zdanie = ''
    while(n):
        zdanie+=wej[randint(0,len(wej)-1)]+' '
        n-=1
    return zdanie

print(zdanie('Single-line comments begin with the hash character (#) and are terminated by the end of line.',5))


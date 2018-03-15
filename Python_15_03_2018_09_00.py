
from random import sample
from random import randint

'''
def L500 (dochody,l_dzieci,l_głów):

    decision = {True:'Otrzymałeś świadczenie', False:'Niestety nie otrzymałeś świadczenia'}
    świadczenie = 0
    dochód_na_głowe = dochody / l_głów

    if (l_dzieci >= 2 and dochód_na_głowe > 800):
        #decision = True
        świadczenie = (l_dzieci-1)*500
        return (decision[True],świadczenie)
    elif(l_dzieci>=2 and dochód_na_głowe<=800):
        #decision = True
        świadczenie = l_dzieci * 500
        return (decision[True], świadczenie)
    elif(l_dzieci < 2 and dochód_na_głowe > 800):
        #decision = False
        świadczenie = 0
        return (decision[False], świadczenie)
    else:
        #decision = True
        świadczenie = 500
        return (decision[True], świadczenie)




def walidacjaWe():
    print('Witaj w programie 500+')
    while(True):
        try:
            dochody = float(input('Podaj dochód rodziny: '))
            l_dzieci = int(input('Podaj liczbę dzieci :'))
            l_głów = int(input('Podaj wielkość rodziny'))
        except:
            print('Podałeś złe dane :')
            continue
        if(dochody >=0 and l_dzieci >= 0 and l_głów > l_dzieci):
            print(L500(dochody, l_dzieci, l_głów))
            break
        else:
            print('ERROR')

walidacjaWe()

#P72

def odl(p1,p2):

    wynik = (((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))**(1/2)
    return wynik

p1=(int(input('Podaj x1')),int(input('Podaj y1')))
p2=(int(input('Podaj x2')),int(input('Podaj y2')))
#p1 = (1,1)
#p2 = (1,1)
print(odl(p1,p2))

#P74
def avg(*arg):
    if(len(arg) == 0):
        return 0
    wynik = 0
    for elem in arg:
        wynik += elem
    return wynik/len(arg)

print(avg(0))




#p76

def html(color_name = 'red',font_size = 15,content = 'Lorem Ipsum'):
    #return('<span style="color:'+ color_name +';font-size:'+font_size+';“>'+content+'</span>')
    return'<span style="color: %s;font-size:%s;“> %s </span>'% (color_name,font_size,content)



color = input('color')
size = input('size')
text = input('text')
if  (color=='' and size=='' and text==''):
    print(html())
else:
    print(html(color,size,text))



#P77 zmienna globalna

def blackORwhite ():
    global color
    if (color == 'white'):
        color = 'black'
        return color
    else:
        color = 'white'
        return color

color = 'white'


print(blackORwhite())
print(blackORwhite())
print(blackORwhite())
print(blackORwhite())
print(blackORwhite())
print(blackORwhite())
print(blackORwhite())
print(blackORwhite())


#p79

wynik = 0

def potega(x,y):
    global wynik
    wynik = (x**y)

potega(3,3)
print(wynik)

napis = 'Lorem Ipsum momento mori'
def my_reverse(a):
    global napis
    napis = ''
    for i,v in enumerate(a):
        napis+= a[(len(a)-1)-i]

my_reverse(napis)
print(napis)

def wordReverse(a):
    global napis
    napis = ' '
    a=a.split(' ')
    for i,v in enumerate(a):
        napis+= a[(len(a)-1)-i]+' '


napis = 'Lorem Ipsum momento mori'
wordReverse(napis)
print(napis)



#P80

def sum_spec(min_wsad,licze):
    zbior = sample(range(0,1000,1),licze)
    lista = []
    suma = 0
    for elem in zbior:
        if elem>=min_wsad:
            lista.append(elem)
            suma +=elem
    return lista,suma

print(sum_spec(1,10))



#  OBIEKTY    ||||||||||||||||||||||||||||||||||||||||||||||||||||||


class Player:
    imie = 'b/d'
    nazwisko = 'b/d'
    pozycja = 'b/d'
    nr = 'b/d'

    def info(self, i , n , p ,nr):
        self.imie = i
        self.nazwisko = n
        self.pozycja = p
        self.nr = nr
        print('%10s %10s %10s %3i' % (i,n,p,nr))


p1 = Player()
print(p1.imie, p1.nazwisko,p1.pozycja,p1.nr)
p1.imie = 'Michał'
print(p1.imie, p1.nazwisko,p1.pozycja,p1.nr)
p1.info('Leo','Messi','stope',15)

p2 = Player()
print(p2.imie, p2.nazwisko,p2.pozycja,p2.nr)


class SalaryCalc:
    def salary(self, salary_net, nazwisko):
        self.salary_net = salary_net
        self.nazwisko = nazwisko

    def show(self):
        return ('%7.2f %7.2f %s' % (self.salary_net, self.salary_net*1.23,self.nazwisko))

test1 = SalaryCalc()
test1.salary(1000.3,'Kowalski')
print(test1.show())


#P81

class Zawodnik:
    def __init__(self,nazwisko, waga, wzrost):
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        #self.bmi()
    def bmi(self):
        print(self.nazwisko,round(self.waga/(self.wzrost/100)**2))

z1 = Zawodnik('Kowalski',64,184)
z2 = Zawodnik('Pawlak',60,189)
z3 = Zawodnik('Kargul',54,162)
z4 = Zawodnik('Nowak',50,159)
z4.bmi()

#P82


class StudentModel:
    def __init__(self, nr, oceny):
        self.nr = nr
        self.oceny = oceny
    def __str__(self):
        return '%s %s' % (self.nr, self.oceny)


class StudentMain:
        ListaStudent = []
        def __init__(self):
            while (True):
                dec = input('A-dodaj , S-szukaj , Q-Wyjście').upper()
                if (dec=='Q'):
                    print('Koniec')
                    break
                elif(dec=='S'):
                    for student in self.ListaStudent:
                        print(student)
                elif(dec=='A'):
                    nr = input('Podaj nr indeksu:')
                    oceny = input('Podaj oceny po przecinku:').split(',')
                    self.ListaStudent.append(StudentModel(nr, oceny))
                    print('Dodano studenta')
                else:
                    print('Podałeś krzaki')

StudentMain()


#ZADANIE DOMOWE - wyszukiwanie po indeksie , i usuwanie konkretniej pozycji


'''
class Lotto:
    def __init__(self):
        self.Losowanie = sample(range(1, 50,1),6)
    def sortowanie(self):
        return sorted(self.Losowanie)
    def __dir__(self):
        return sorted(self.Losowanie)


los1 = Lotto()
print(dir(los1))
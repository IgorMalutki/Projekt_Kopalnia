import json
import pymysql
import sqlite3
import sys
from urllib.request import Request, urlopen
from pprint import pprint
from os import getcwd,chdir,listdir
from threading import Timer
import time
import matplotlib.pyplot as plt
import numpy as np
import datetime

class DBConnect:
    def __init__(self):
         try:
            self.conn = pymysql.connect('localhost','root','Alaskan1!','kopalnie',charset='utf8')
            print('Connected')
            self.c = self.conn.cursor()
            self.menu()
         except:
             print('Złe dane')
    def menu(self):
            while(True):
                dec = input('L-lista górników, I-insert, D-delete ,Q-exit, C-czytamy API, S-statystyki, W-wykresy' ).upper()
                if(dec=='L'):
                    self.select()
                elif(dec=='I'):
                    self.insert()
                    self.menu()
                elif(dec=='D'):
                    self.delete()
                elif(dec=='C'):
                    id_kopalni = input('Podaj ID kopalni, 1-Etermine 2-Nanopool 3-Dwarfpool :')
                    if id_kopalni== '1':
                        self.czytamy_API_Ethermine()

                    elif id_kopalni=='2':
                        pass
                    elif id_kopalni=='3':
                        self.czytamy_API_DwarfPoll()
                    else:
                        break
                elif(dec=='S'):
                    self.wyświetlamy_Średni_Zarobek()
                elif(dec=='W'):
                    self.rysujemy_Wykresy(miner0E)
                elif(dec=='Q'):
                    print('Koniec')
                    break
                else:
                    ('Podałeś krzaki')
    def insert(self):
        miner_address = input('Podaj aadres portfela :')
        id_kopalni = input('Podaj ID kopalni, 1-Etermine 2-Nanopool 3-Dwarfpool :')
        self.c.execute('INSERT INTO miners (miner_address,pool_id) VALUES (%s, %s)',(miner_address,id_kopalni))
        self.conn.commit()

    def select(self):
        self.c.execute('SELECT m.miner_id,m.miner_address,p.pool_name FROM miners as m NATURAL JOIN pool as p')
        gornicy = self.c.fetchall()
        for elem in gornicy:
            print('%3i | %50s | %5s' % (elem[0],elem[1],elem[2]))

    def delete(self):
        self.select()
        miner_id = input('Podaj numer górnika do usunięcia :')
        self.c.execute('DELETE FROM miners WHERE miner_id=%s',miner_id)
        if input('Na pewno ? T/N').upper() == 'T':
            self.conn.commit()
            print('Usunieto')
        else:
            self.conn.rollback()
            print('Nie usunieto')

    def czytamy_API_Ethermine(self):
        self.c.execute('SELECT * FROM miners WHERE pool_id=1')
        self.lista_minerow = self.c.fetchall()
        for elem in self.lista_minerow:
            url = Request("https://api.ethermine.org/miner/:" + elem[0] + "/currentStats", headers={'User-agent': ''})
            data = urlopen(url).read()  # czyta API z określonego end-pointu , domyślnie jest to obiekt tybu "byte" <class,byte>
            print(data)
            data_json = json.loads(data)
            self.c.execute(
                "INSERT INTO miner(miner_address,coin_id,pool_id,response_time,last_seen,reportedHashrate,currentHashrate,"
                "validShares,invalidShares,staleShares,averageHashrate,activeWorkers,unpaid,unconfirmed,coinsPerMin,"
                "usdPerMin,btcPerMin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (elem[0], 'ETH', 1, data_json['data']['time'], data_json['data']['lastSeen'],
                 data_json['data']['reportedHashrate'], data_json['data']['currentHashrate'],
                 data_json['data']['validShares'],
                 data_json['data']['invalidShares'], data_json['data']['staleShares'],
                 data_json['data']['averageHashrate'],
                 data_json['data']['activeWorkers'], data_json['data']['unpaid'], data_json['data']['unconfirmed'],
                 data_json['data']['coinsPerMin'], data_json['data']['usdPerMin'], data_json['data']['btcPerMin']))
            self.conn.commit()
        plik_danych = open("miner_json.txt", "a")  # dopisywanie kolejnych stringów
        plik_danych.writelines(data_json)  # dopisuje do pliku kolejne porcje danych
        plik_danych.close()  # zamyka plik'''


    def czytamy_API_DwarfPoll(self):
        self.c.execute('SELECT * FROM miners where pool_id=3')
        self.lista_minerow = self.c.fetchall()
        for elem in self.lista_minerow:
            url = Request("http://dwarfpool.com/eth/api?wallet=" + elem[0] + "&mail@example.com")
            data = urlopen(url).read()
            print(data)
            data_json = json.loads(data)
            self.c.execute(
                "INSERT INTO miner_d (miner_address,coin_id,pool_id,earning_24_hours,immature_earning,last_payment_amount,"
                "total_hashrate,total_hashrate_calculated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (elem[0], 'ETH', 3, data_json['earning_24_hours'],
                 data_json['immature_earning'], data_json['last_payment_amount'], data_json['total_hashrate'],
                 data_json['total_hashrate_calculated']))
        plik_danych = open("minerD_json.txt", "a")  # dopisywanie kolejnych stringów
        plik_danych.writelines(data_json)  # dopisuje do pliku kolejne porcje danych
        plik_danych.close()  #
        self.conn.commit()

    def wyświetlamy_Średni_Zarobek(self):
        self.c.execute('SELECT * FROM miners')
        self.lista_minerow = self.c.fetchall()
        for elem in self.lista_minerow:
            if elem[1]==1:
                self.c.execute("SELECT usdPerMin*60*24*30/averageHashrate*1000000 FROM miner WHERE miner_address='"+elem[0]+"'")
                data = self.c.fetchall();
                suma = 0
                for i,elem1 in enumerate (data):
                    suma +=data[i][0]
                average = suma/len(data)
                print("Miner ",elem[0]," zarabia średnio :",average,"USD miesięcznie z Mhs")
            elif elem[1]==2:
                pass
            else:
                self.c.execute("SELECT earning_24_hours*30*600/total_hashrate FROM miner_d WHERE miner_address='"+elem[0]+"'"
                "and total_hashrate != 0")
                data = self.c.fetchall();
                suma = 0
                for i,elem1 in enumerate (data):
                    suma +=data[i][0]
                average = suma/len(data)
                print("Miner ",elem[0]," zarabia średnio :",average,"USD miesięcznie z Mhs")

    def rysujemy_Wykresy(self,miner):
        self.c.execute('SELECT * FROM miners WHERE pool_id=1')
        self.lista_minerow = self.c.fetchall()
        for elem in self.lista_minerow:
            self.c.execute(
            "SELECT averageHashrate/1000000,response_time FROM miner WHERE miner_address ='" + elem[0] + "' and averageHashrate IS NOT NULL and "
            "response_time IS NOT NULL")
            data = self.c.fetchall();
            x = [item[1] for item in data]
            y = [item[0] for item in data]
            czas = []
            for elem in x:
                elem = datetime.date.fromtimestamp(elem)
                splitDate = str(elem).split("-");
                strDate = splitDate[0] + "-" + splitDate[1] + "-" + splitDate[2]
                czas.append(strDate)
            plt.plot(czas, y, label=miner)
            plt.legend()
            plt.xlabel("Czas")
            plt.xticks(rotation='vertical')
            plt.ylabel("MHs")
            plt.title("Średni Hashrate")
            plt.grid(True)
            plt.show()


miner0E = "0x5ca6304461560bD95B440466D180e90632099C33"
miner1E = "0x5063a979617df7bcf899665f797f3750fa57611c"
miner2E = "0xdc6ae013c81ed9d5d7086da8b42af3d4efe733fd"
miner3E = "0xc7fe69ed4919a7d26f22105ce020ca865b63f7cf"
miner4E = "0xf7ec3800df78ab77990c2d5aa92554ecf934e30e"
miner5E = "0x875dc0445fbe1af5c4fd262bdcfe79c079a8ac86"
miner6E = "0x0a0216C1502625CE14907fa2f8F2188BEee5E8D8"
miner7E = "0x0b467c4F86976305ed567D8e2dA27F04bC8dcc39"
miner8E = "0x5be0d21cd3624ade634f5a7c118b950cb4449a0b"

miner0N = "0xe4550c3457ed81afbd87b94540108e29fe5406f0"
miner1N = "0x964b5539c7b937d44dce69ab74f309dd1754386c"
miner2N = "0x0a09e76547e37c52874ee8484300547e4fa7f952"


miner0D = "82b83b2fc6ef0c8c79926ba643858f14c739caf0"
miner1D = "d9533a9b9880bd50d187d7fa6832adee1b967dd6"
miner2D = "69aEE08CF56a8000456360d1ae6E0C4f673B488b"
miner3D = "7a6d70D0D850f309B2fc397BA619a8EF4311CF30"
miner4D = "910DDFD390402DC845C468FC377010FB7B566ACE"
miner5D = "0439E3Df67Eb69912bEc0e3B659135ED9553a700"
miner6D = "34FA6277C5A1C4956B555A87FF6B58E208465509"
miner7D = "45ee8f010a6e4b3123b7829328c9140812dc10b7"
miner8D = "1809433f68C68439D40c84ac81330824f542D092"  # zrzuca błędy

lista_minerow_D = [miner0D,miner1D,miner2D,miner3D,miner4D,miner5D,miner6D,miner7D]
lista_minerow_E = [miner0E,miner1E,miner2E,miner3E,miner4E,miner5E,miner6E,miner7E,miner8E]



def czytamy_API_Nanopool(miner,coin,pool):
    url2 = Request("https://api.nanopool.org/v1/eth/avghashrate/:"+miner+"/:24",headers={'User-agent': ''})
    print ("https://api.nanopool.org/v1/eth/avghashrate/:"+miner+"/:24")
    url3 = Request("https://api.nanopool.org/v1/eth/pool/activeworkers",headers={'User-Agent':''})
    url5 = Request("https://api.nanopool.org/v1/eth/hashrate/:"+miner,headers={'User-Agent':''})
    url1 = Request("https://api.nanopool.org /v1/eth/balance/:"+miner,headers={'User-agent': 'Mozilla/4.0 (compatible; pynanopoolapi; ' +
                          str(sys.platform) + '; ' + str(sys.version).replace('\n', '') + ')'})

    data = urlopen(url2).read()
    print(data)


o = DBConnect()

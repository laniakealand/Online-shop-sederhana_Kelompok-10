import csv


def tabel_girlband():
    data_tabel_girlband= []
    with open('data_girlband.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_tabel_girlband.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU ROCK'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_tabel_girlband)):
        print(f'| {data_tabel_girlband[i][0]:^8} | {data_tabel_girlband[i][1]:^45} | {data_tabel_girlband[i][2]:^8} | {data_tabel_girlband[i][3]:^8} | {data_tabel_girlband[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))
        
def tabel_band():
    data_tabel_band= []
    with open('data_band.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_band.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU ROCK'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_tabel_band)):
        print(f'| {data_tabel_band[i][0]:^8} | {data_tabel_band[i][1]:^45} | {data_tabel_band[i][2]:^8} | {data_tabel_band[i][3]:^8} | {data_tabel_band[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

def tabel_2021():
    data_tabel_2021= []
    with open('data_2021_keatas.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_tabel_2021.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU ROCK'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_tabel_2021)):
        print(f'| {data_tabel_2021[i][0]:^8} | {data_tabel_2021[i][1]:^45} | {data_tabel_2021[i][2]:^8} | {data_tabel_2021[i][3]:^8} | {data_tabel_2021[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))
        

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import csv
import os


#data_lagu_rock = pd.read_csv('data_rock.csv')
#data_lagu_pop = pd.read_csv('data_pop.csv')
#data_lagu_kpop = pd.read_csv('data_kpop.csv')
#data_lagu_semua = pd.read_csv('data_semua.csv')

#TABEL ROCK
def tabel_rock():
    data_lagu_rock = []
    with open('data_rock.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_lagu_rock.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU ROCK'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_lagu_rock)):
        print(f'| {data_lagu_rock[i][0]:^8} | {data_lagu_rock[i][1]:^45} | {data_lagu_rock[i][2]:^8} | {data_lagu_rock[i][3]:^8} | {data_lagu_rock[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL POP
def tabel_pop():
    data_lagu_pop = []
    with open('data_pop.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_lagu_pop.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU POP'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_lagu_pop)):
        print(f'| {data_lagu_pop[i][0]:^8} | {data_lagu_pop[i][1]:^45} | {data_lagu_pop[i][2]:^8} | {data_lagu_pop[i][3]:^8} | {data_lagu_pop[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL K-POP
def tabel_kpop():
    data_lagu_kpop = []
    with open('data_kpop.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_lagu_kpop.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU POP'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_lagu_kpop)):
        print(f'| {data_lagu_kpop[i][0]:^8} | {data_lagu_kpop[i][1]:^45} | {data_lagu_kpop[i][2]:^8} | {data_lagu_kpop[i][3]:^8} | {data_lagu_kpop[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))


#TABEL BOYBAND
def tabel_boyband():
    data_lagu_boyband = []
    with open('data_boyband.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_lagu_boyband.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU BOYBAND'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_lagu_boyband)):
        print(f'| {data_lagu_boyband[i][0]:^8} | {data_lagu_boyband[i][1]:^45} | {data_lagu_boyband[i][2]:^8} | {data_lagu_boyband[i][3]:^8} | {data_lagu_boyband[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL GIRLBAND
def tabel_girlband():
    data_tabel_girlband= []
    with open('data_girlband.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_tabel_girlband.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU GIRLBAND'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_tabel_girlband)):
        print(f'| {data_tabel_girlband[i][0]:^8} | {data_tabel_girlband[i][1]:^45} | {data_tabel_girlband[i][2]:^8} | {data_tabel_girlband[i][3]:^8} | {data_tabel_girlband[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL BAND       
def tabel_band():
    data_tabel_band= []
    with open('data_band.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_band.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU BAND'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_tabel_band)):
        print(f'| {data_tabel_band[i][0]:^8} | {data_tabel_band[i][1]:^45} | {data_tabel_band[i][2]:^8} | {data_tabel_band[i][3]:^8} | {data_tabel_band[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL TAHUN 2000-2010
def tabel_lagu2000():
    data_lagu_2000 = []
    with open('data_2000-2010.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_lagu_2000.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU TAHUN 2000-2010'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_lagu_2000)):
        print(f'| {data_lagu_2000[i][0]:^8} | {data_lagu_2000[i][1]:^45} | {data_lagu_2000[i][2]:^8} | {data_lagu_2000[i][3]:^8} | {data_lagu_2000[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL TAHUN 2011-2020
def tabel_lagu2011():
    data_lagu_2011 = []
    with open('data_2011-2020.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_lagu_2011.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU TAHUN 2011-2020'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_lagu_2011)):
        print(f'| {data_lagu_2011[i][0]:^8} | {data_lagu_2011[i][1]:^45} | {data_lagu_2011[i][2]:^8} | {data_lagu_2011[i][3]:^8} | {data_lagu_2011[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL LAGU DIATAS 2021
def tabel_2021():
    data_tabel_2021= []
    with open('data_2021_keatas.csv', 'r') as file:
        reader = csv.reader(file)
          # Membaca baris header (kolom)
        for row in reader:
            data_tabel_2021.append(row)
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU DIATAS TAHUN 2021'.center(113))
    print('')
    print(('-'*113).center(113))
    #genre,name,price,year,link
    for i in range(len(data_tabel_2021)):
        print(f'| {data_tabel_2021[i][0]:^8} | {data_tabel_2021[i][1]:^45} | {data_tabel_2021[i][2]:^8} | {data_tabel_2021[i][3]:^8} | {data_tabel_2021[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))
        
# Fungsi Menampilkan Produk
def display_products(products):
    print("== Produk Tersedia ==:")
    print("---------------------")
    for _, product in products.iterrows():
        print(f"{products['genre']}, {products['name']}, {products['year']}, {products['link']}: Rp{products['price']}")

# Fungsi Genre
def genre():
    print("1. Rock")
    print("2. Pop")
    print("3. K-Pop")

    g = int(input("Masukkan pilihan anda: "))
    # Looping
    if g == 1:
        print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
        tabel_rock()
        input("Tekan ENTER untuk lanjut \n")
    elif g == 2:
        print("Genre musik pop adalah salah satu genre musik yang terkenal. Bahkan genre musik pop bisa dibilang sebagai aliran musik paling populer dan paling banyak dinyanyikan oleh penyanyi dan band di seluruh dunia.")
        tabel_pop()
        input("Tekan ENTER untuk lanjut \n")
    elif g == 3:
        print("Genre musik k-pop adalah genre musik populer yang berasal dari Korea Selatan. Lagu-lagu K-pop banyak dipengaruhi oleh berbagai genre musik, seperti hip-hop, electronic dance, jazz, dan rock.")
        tabel_kpop()
        input("Tekan ENTER untuk lanjut \n")
    else:
        print("INPUT SALAH")
        genre()

# Fungsi Penyanyi
def penyanyi():
    print("1. Boyband")
    print("2. Girlband")
    print("3. Band")

    t = int(input("Masukkan pilihan anda: "))
    # Looping
    if t == 1:
        print("Musik ini adalah musik yang dibawakan oleh grup para pria")
        tabel_boyband()
        input("Tekan ENTER untuk lanjut \n")
    elif t == 2:
        print("Musik ini adalah musik yang dibawakan oleh grup para wanita")
        tabel_girlband()
        input("Tekan ENTER untuk lanjut \n")
    elif t == 3:
        print("Musik ini adalah musik yang dibawakan menggunakan berbagai alat musik")
        tabel_band()
        input("Tekan ENTER untuk lanjut \n")
    else:
        print("INPUT SALAH")
        genre()

# Fungsi Tahun
def tahun():
    print("1. Tahun 2000-2010")
    print("2. Tahun 2011-2020")
    print("3. >=Tahun 2021")

    t = int(input("Masukkan pilihan anda: "))
    # Looping
    if t == 1:
        print("Musik ini adalah musik pada era 2000-2010")
        tabel_lagu2000()
        input("Tekan ENTER untuk lanjut \n")
    elif t == 2:
        print("Musik ini adalah musik pada era 2011-2020")
        tabel_lagu2011()
        input("Tekan ENTER untuk lanjut \n")
    elif t == 3:
        print("Musik ini adalah musik pada era lebih dari 2021")
        tabel_kpop()
        input("Tekan ENTER untuk lanjut \n")
    else:
        print("INPUT SALAH")
        genre()

# Fungsi Menu Awal
def menu_awal():
    print("Selamat Datang di Program Online Shop Sederhana".center(115))
    print("===============================================".center(115))
    print("Program ini merupakan program jual beli album lagu secara online".center(115))
    
    print("1. Genre")
    print("2. Penyanyi")
    print("3. Tahun")
    print("4. Keluar")

    pilihan = int(input("Masukkan pilihan anda: "))
    # Looping
    if pilihan == 1:
        genre()
    elif pilihan == 2:
        penyanyi()
    elif pilihan == 3:
        tahun()
    elif pilihan == 4:
        print("\n TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI \n")
        pass
    else:
        menu_awal()

 

# Menjalankan program
menu_awal()
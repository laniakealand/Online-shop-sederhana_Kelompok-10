import pandas as pd
data_lagu = pd.read_csv('data_lagu.txt')


def menu_awal():
    print("Selamat Datang di Program Online Shop Sederhana")
    print("===============================================")
    print("Program ini merupakan program jual beli album lagu secara online")
    
    print("1. Genre")
    print("2. Penyanyi")
    print("3. Tahun")

def Genre_Rock():
        print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
        print(data_lagu)
        print("1. Artis")
        print("2. Judul")
        print("3. Tahun")
        print("4. Keluar")
        pass

import pandas as pd

def artis_rock():
    pencarian_artis = input("Masukkan artis yang ingin Anda cari: ")
    # Membaca data dari file txt
    df = pd.read_csv('data_lagu.txt', delimiter=',')
    # Menggunakan fitur str.strip() untuk menghilangkan spasi di sekitar nilai kolom
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    # Menggunakan fitur str.lower() untuk memastikan pencarian tidak case-sensitive
    artis_df = df[df['Artis'].str.lower() == pencarian_artis.lower()]
    if not artis_df.empty:
        print(artis_df)
    else:
        print("Maaf lagu yang Anda cari tidak tersedia.")




menu_awal()
pilihan_awal = input("Masukkan filter yang anda inginkan: ")    
if pilihan_awal == "1":
    def Genre():
        print("Selamat Datang di Program Online Shop Sederhana")
        print("===============================================")
        print("Program ini merupakan program jual beli album lagu secara online")        
        print("Pilihan genre lagu yang ditawarkan pada program ini berupa lagu Rock, Pop dan K-Pop.")
        #menampilkan info genre lau
        print("Informasi Genre Lagu")
        print("1. Rock")
        print("2. Pop")
        print("3. K-Pop")
        print("4. Keluar")
    Genre()               
    pilihan_genre = input("Masukkan genre lagu yang anda pilih: ")

    if pilihan_genre == "1":
        Genre_Rock()
        pilihan_filter_rock = input("Masukkan filter yang ingin anda pilih: ")

        if pilihan_filter_rock == "1":
            artis_rock() 





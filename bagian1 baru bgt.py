import pandas as pd



def menu_awal():
    print("Selamat Datang di Program Online Shop Sederhana")
    print("===============================================")
    print("Program ini merupakan program jual beli album lagu secara online")
    
    print("1. Genre")
    print("2. Penyanyi")
    print("3. Tahun")
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
    def Genre_Rock():
        print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
        list_lagu_rock = pd.read_csv('data_lagu.csv')
        print(list_lagu_rock)
        print("1. Artis")
        print("2. Judul")
        print("3. Tahun")
        print("4. Keluar")
        def Artis_Rock():
            pencarian_artis = input("Masukkan artis yang ingin anda cari: ")
            for lagu in data_lagu.iterrows():
                if lagu['artis'] == pencarian_artis:
                    print("Artis:", lagu['artis'])
                    print("Judul:", lagu['judul'])
                    print("Tahun:", lagu['tahun'])
pilihan_genre = input("Masukkan genre lagu yang anda pilih: ")
if pilihan_genre == "1":
    Genre_Rock()
pilihan_filter_rock = input("Masukkan filter yang ingin anda pilih: ")
if pilihan_filter_rock == "1":
    Artis_Rock() #ini error bagian artis rock doang nangis dikit yaudah bismillah dalam nama tuhan yesus





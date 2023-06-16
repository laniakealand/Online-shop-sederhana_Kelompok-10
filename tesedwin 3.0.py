import pandas as pd
import csv
import os
import random



# Define the shopping cart as a global variable
cart = []

# Load song data from CSV files
data_lagu_rock = pd.read_csv('data_rock.csv')
data_lagu_pop = pd.read_csv('data_pop.csv')
data_lagu_kpop = pd.read_csv('data_kpop.csv')
data_lagu_boyband = pd.read_csv('data_boyband.csv')
data_lagu_girlband = pd.read_csv('data_girlband.csv')
data_lagu_band = pd.read_csv('data_band.csv')
data_lagu_2000_2010 = pd.read_csv('data_2000-2010.csv')
data_lagu_2011_2020 = pd.read_csv('data_2011-2020.csv')
data_lagu_2021_2023 = pd.read_csv('data_2021-keatas.csv')


#TABEL ROCK
def tabel_rock():
    data_lagu_rock = []
    with open('data_rock.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_rock.append(header)
        
        # Membaca baris data
        for row in reader:
            data_lagu_rock.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU ROCK'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu rock
    for i in range(1, len(data_lagu_rock)):
        print(f'| {i:^4} | {data_lagu_rock[i][0]:^8} | {data_lagu_rock[i][1]:^45} | {data_lagu_rock[i][2]:^8} | {data_lagu_rock[i][3]:^8} | {data_lagu_rock[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL POP
def tabel_pop():
    data_lagu_pop = []
    with open('data_pop.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_pop.append(header)
        
        # Membaca baris data
        for row in reader:
            data_lagu_pop.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU POP'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu pop
    for i in range(1, len(data_lagu_pop)):
        print(f'| {i:^4} | {data_lagu_pop[i][0]:^8} | {data_lagu_pop[i][1]:^45} | {data_lagu_pop[i][2]:^8} | {data_lagu_pop[i][3]:^8} | {data_lagu_pop[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL K-POP
def tabel_kpop():
    data_lagu_kpop = []
    with open('data_kpop.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_kpop.append(header)
        
        # Membaca baris data
        for row in reader:
            data_lagu_kpop.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU KPOP'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu kpop
    for i in range(1, len(data_lagu_kpop)):
        print(f'| {i:^4} | {data_lagu_kpop[i][0]:^8} | {data_lagu_kpop[i][1]:^45} | {data_lagu_kpop[i][2]:^8} | {data_lagu_kpop[i][3]:^8} | {data_lagu_kpop[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL BOYBAND
def tabel_boyband():
    data_lagu_boyband = []
    with open('data_boyband.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_boyband.append(header)
        
        # Membaca baris data
        for row in reader:
            data_lagu_boyband.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU BOYBAND'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu boyband
    for i in range(1, len(data_lagu_boyband)):
        print(f'| {i:^4} | {data_lagu_boyband[i][0]:^8} | {data_lagu_boyband[i][1]:^45} | {data_lagu_boyband[i][2]:^8} | {data_lagu_boyband[i][3]:^8} | {data_lagu_boyband[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL GIRLBAND
def tabel_girlband():
    data_lagu_girlband = []
    with open('data_girlband.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_girlband.append(header)
        
        # Membaca baris data
        for row in reader:
            data_lagu_girlband.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU GIRLBAND'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu girlband
    for i in range(1, len(data_lagu_girlband)):
        print(f'| {i:^4} | {data_lagu_girlband[i][0]:^8} | {data_lagu_girlband[i][1]:^45} | {data_lagu_girlband[i][2]:^8} | {data_lagu_girlband[i][3]:^8} | {data_lagu_girlband[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL BAND       
def tabel_band():
    data_lagu_band = []
    with open('data_band.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_band.append(header)
        
        # Membaca baris data
        for row in reader:
            data_lagu_band.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU BAND'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu band
    for i in range(1, len(data_lagu_band)):
        print(f'| {i:^4} | {data_lagu_band[i][0]:^8} | {data_lagu_band[i][1]:^45} | {data_lagu_band[i][2]:^8} | {data_lagu_band[i][3]:^8} | {data_lagu_band[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL TAHUN 2000-2010
def tabel_lagu2000():
    data_lagu_2000_2010 = []
    with open('data_2000-2010.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_2000_2010.append(header)
        
        # Membaca baris data
        for row in reader:
           data_lagu_2000_2010.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU TAHUN 2000-2010'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu tahun 2000-2010
    for i in range(1, len(data_lagu_2000_2010)):
        print(f'| {i:^4} | {data_lagu_2000_2010[i][0]:^8} | {data_lagu_2000_2010[i][1]:^45} | {data_lagu_2000_2010[i][2]:^8} | {data_lagu_2000_2010[i][3]:^8} | {data_lagu_2000_2010 [i][4]:^28} |'.center(113))
        print(('-'*113).center(113))

#TABEL TAHUN 2011-2020
def tabel_lagu2011():
    data_lagu_2011_2020 = []
    with open('data_2011-2020.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_2011_2020.append(header)
        
        # Membaca baris data
        for row in reader:
           data_lagu_2011_2020.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU TAHUN 2000-2010'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu tahun 2011-2020
    for i in range(1, len(data_lagu_2011_2020)):
        print(f'| {i:^4} | {data_lagu_2011_2020[i][0]:^8} | {data_lagu_2011_2020[i][1]:^45} | {data_lagu_2011_2020[i][2]:^8} | {data_lagu_2011_2020[i][3]:^8} | {data_lagu_2011_2020[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))


#TABEL LAGU DIATAS 2021
def tabel_lagu2021():
    data_lagu_2021_2023 = []
    with open('data_2021-keatas.csv', 'r') as file:
        reader = csv.reader(file)
        # Membaca baris header (kolom)
        header = next(reader)
        data_lagu_2021_2023.append(header)
        
        # Membaca baris data
        for row in reader:
           data_lagu_2021_2023.append(row)
    
    print('')
    print('TABEL'.center(113))
    print('DATA LAGU TAHUN 2021-2023'.center(113))
    print('')
    print(('-'*113).center(113))
    
    # Header
    print(f'| {"No":^4} | {header[0]:^8} | {header[1]:^45} | {header[2]:^8} | {header[3]:^8} | {header[4]:^28} |'.center(113))
    print(('-'*113).center(113))
    
    # Data lagu tahun 2021-2023
    for i in range(1, len(data_lagu_2021_2023)):
        print(f'| {i:^4} | {data_lagu_2021_2023[i][0]:^8} | {data_lagu_2021_2023[i][1]:^45} | {data_lagu_2021_2023[i][2]:^8} | {data_lagu_2021_2023[i][3]:^8} | {data_lagu_2021_2023[i][4]:^28} |'.center(113))
        print(('-'*113).center(113))
 
# Fungsi Menampilkan Produk
def display_products(products):
    print("== Produk Tersedia ==:")
    print("---------------------")
    for _, product in products.iterrows():
        print(f"{product['genre']}, {product['name']}, {product['year']}, {product['link']}: Rp{product['price']}")

# Fungsi Genre
def genre():
    print("1. Rock")
    print("2. Pop")
    print("3. K-Pop")
    print("4. Keluar")

    g = int(input("Masukkan pilihan anda: "))
    
    if g == 1:
        print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
        tabel_rock()
        add_to_cart(data_lagu_rock)
    elif g == 2:
        print("Genre musik pop adalah salah satu genre musik yang terkenal. Bahkan genre musik pop bisa dibilang sebagai aliran musik paling populer dan paling banyak dinyanyikan oleh penyanyi dan band di seluruh dunia.")
        tabel_pop()
        add_to_cart(data_lagu_pop)
    elif g == 3:
        print("Genre musik k-pop adalah genre musik populer yang berasal dari Korea Selatan. Lagu-lagu K-pop banyak dipengaruhi oleh berbagai genre musik, seperti hip-hop, electronic dance, jazz, dan rock.")
        tabel_kpop()
        add_to_cart(data_lagu_kpop)
    elif g == 4:
        print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI\n")
        pass
    else:
        print("INPUT SALAH")
        genre()

# Fungsi Penyanyi
def penyanyi(): 
    print("1. Boyband")
    print("2. Girlband")
    print("3. Band")
    print("4. Keluar")

    p = int(input("Masukkan pilihan anda: "))
    # Looping
    if p == 1:
        print("Musik ini adalah musik yang dibawakan oleh grup para pria")
        tabel_boyband()
        add_to_cart(data_lagu_boyband)
    elif p == 2:
        print("Musik ini adalah musik yang dibawakan oleh grup para wanita")
        tabel_girlband()
        add_to_cart(data_lagu_girlband)
    elif p == 3:
        print("Musik ini adalah musik yang dibawakan menggunakan berbagai alat musik")
        tabel_band()
        add_to_cart(data_lagu_band)
    elif p == 4:
        print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI\n")
        pass
    else:
        print("INPUT SALAH")
        penyanyi()

# Fungsi Tahun
def tahun():
    print("1. Tahun 2000-2010")
    print("2. Tahun 2011-2020")
    print("3. >=Tahun 2021")
    print("4. Keluar")

    t = int(input("Masukkan pilihan anda: "))
    # Looping
    if t == 1:
        print("Musik ini adalah musik pada era 2000-2010")
        tabel_lagu2000()
        add_to_cart(data_lagu_2000_2010)
    elif t == 2:
        print("Musik ini adalah musik pada era 2011-2020")
        tabel_lagu2011()
        add_to_cart(data_lagu_2011_2020)
    elif t == 3:
        print("Musik ini adalah musik pada era lebih dari 2021")
        tabel_lagu2021()
        add_to_cart(data_lagu_2021_2023)
    elif t == 4:
        print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI\n")
        pass
    else:
        print("INPUT SALAH")
        tahun()

# Fungsi untuk menambahkan lagu ke keranjang
def add_to_cart(products):
    pilihan = int(input("Masukkan nomor lagu yang ingin ditambahkan ke keranjang: "))
    if pilihan < 1 or pilihan > len(products):
        print("Nomor lagu tidak valid!")
        add_to_cart(products)
    else:
        song = products.loc[pilihan - 1, :]
        cart.append(song)
        print(f"Lagu {song['name']} telah ditambahkan ke keranjang!")
        input("Tekan ENTER untuk lanjut \n")

# Fungsi untuk menghapus item dari keranjang
def remove_from_cart():
    if not cart:
        print("Keranjang masih kosong!")
        input("Tekan ENTER untuk lanjut \n")
    else: 
        print("== Isi Keranjang ==")
        print("-------------------")
        for i, song in enumerate(cart):
            print(f"{i+1}. {song['genre']}, {song['name']}, {song['year']}, {song['link']}: Rp{song['price']}")
        pilihan = int(input("Masukkan nomor lagu yang ingin dihapus dari keranjang: "))
        if pilihan < 1 or pilihan > len(cart):
            print("Nomor lagu tidak valid!")
            remove_from_cart()
        else:
            song = cart.pop(pilihan - 1)
            print(f"Lagu {song['name']} telah dihapus dari keranjang!")
            input("Tekan ENTER untuk lanjut \n")

# Fungsi untuk menampilkan isi keranjang
def display_cart():
    if not cart:
        print("Keranjang masih kosong!")
    else:
        print("== Isi Keranjang ==")
        print("-------------------")
        for i, song in enumerate(cart):
            print(f"{i+1}. {song['genre']}, {song['name']}, {song['year']}, {song['link']}: Rp{song['price']}")
    input("Tekan ENTER untuk lanjut \n")

# Fungsi untuk melanjutkan pembayaran
def checkout():
    global total_price
    if not cart:
        print("Keranjang masih kosong!")
        input("Tekan ENTER untuk lanjut \n")
        menu_awal()
    else:
        print("")
        print("=======MY LIST=======")
        print("----------------------")
        total_price = sum(song['price'] for song in cart)
        for song in cart:
            print(f"{song['name']}: Rp{song['price']}")
        print(f"Total Harga: Rp{total_price}")
        input("Tekan ENTER untuk lanjut \n")
        datapengguna()
        ongkir()
        metodebayar()
        # Reset the cart
        cart.clear()

#Menu Pembelian
def kembali_pembelian():
    pilihan_kembali = str(input("Apakah anda ingin membeli lagi? (ya/tidak): "))
    while True:
                if pilihan_kembali == "ya":
                    menu_awal()
                elif pilihan_kembali == "tidak":
                    print("1. Keranjang")
                    print("2. Hapus dari Keranjang")
                    print("3. Lanjutkan pembayaran")
                    print("4. Keluar")
                    pilihan_pembelian = int(input("Masukkan pilihan anda: "))
                    if pilihan_pembelian == 1:
                        display_cart()
                    elif pilihan_pembelian == 2: 
                        remove_from_cart()
                    elif pilihan_pembelian == 3:
                        checkout()
                        break
                    elif pilihan_pembelian == 4:
                        print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI\n")
                        break
                    else:
                        print("INPUT SALAH")
                        kembali_pembelian()

# Input Data User
def datapengguna():
    global nama
    global phone
    global rumah
    global kota
    
    
    print('                 DATA USER                ')
    nama = input('Masukkan Nama Anda               : ')
    for name in nama:
        if name.isdigit():
            print("Tolong Masukan Dengan Huruf")
            datapengguna()
    phone = input('Masukkan No HP Anda             :+62 ')
    rumah = input('Masukkan Alamat Anda            : ')
    kota  = input('Masukkan Kota Anda              : ')
    print()
    print('=========================================')
    print()
                        
#Struk
def struk():
    # kode pelunasan
    lunas = random.randrange(55555, 77777, 10)
    print("Kode Pembayaran anda adalah", lunas)
    print("Silahkan membayar ke No. Akun tersebut")
    print()

    while True:
        bayarr = int(input("Masukan Kode Pelunasan: "))
        if bayarr == lunas:
            print("Pembayaran Dengan No Akun", bayarr, "Berhasil. \n Hubungi Admin Jika Ada Kendala")
            break
        else:
            print("Maaf, Kode Pelunasan Salah!")

    # Template Struk
    print()
    print('==============================================================')
    print("                      STRUK PEMBELIAN")
    print('==============================================================')
    print()
    print(" Nama                : ", nama)
    print(" Nomor HP            :  +62",phone)
    print(" Alamat              : ", rumah, ",", kota)
    print(" Kode Pembayaran     : ", bayarr)
    print(" Nominal Bayar       :  Rp.", pay)
    print("==============================================================")
    print("                        TERIMA KASIH                          ")
    print("==============================================================")
    print()
    print("Terimakasih pesanan akan dikirim\n"
          "Apabila belum terkirim dapat hubungi admin.")
    pass

#Ongkos Kirim
# Kota Jogja
ongkir_jgj = 5000  
# Kota Semaarang
ongkir_smg = 7000
# Kota Surabaya
ongkir_sby = 9000
# Kota Malang 
ongkir_mlg = 11000
# Kota Salatiga
ongkir_slt = 6000
# alamat ongkir
def ongkir():
    global pay
    print('barang anda akan diantarkan jika anda berada pada kota jangkauan')
    kota = input("Kota (Jogja/Semarang/Surabaya/Malang/Salatiga) : ")
    if kota == "Jogja":
        pay = ongkir_jgj + total_price
        print("Total yang harus dibayarkan : Rp.", pay)
        ()
    elif kota == "Semarang":
        pay = ongkir_smg + total_price
        print("Total yang harus dibayarkan : Rp.", pay)
        ()
    elif kota == "Surabaya":
        pay = ongkir_slt + total_price
        print("Total yang harus dibayarkan :Rp. ", pay)
        ()
    elif kota == "Malang":
        pay = ongkir_mlg + total_price
        print("Total yang harus dibayarkan :Rp. ", pay)
        ()
    elif kota == "Salatiga":
        pay = ongkir_slt + total_price
        print("Total yang harus dibayarkan :Rp. ", pay)
        ()
    else :
        print("Kota yang dicantumkan tidak terdeteksi")

# Menu Metode Bayar
def metodebayar():
    global bayar
    print("Pilih Metode Pembayaran\n"
              "[1] Gopay\n"
              "[2] Bank Mandiri\n"
              "[3] Bank BNI\n")

    # Pengguna memilih metode pembayaran
    bayar = int(input('>>'))
    if bayar == 1:
        print('silahkan lakukan pembayaran ke akun gopay kami')
        print('081563184352 A.N. Gabeta')
        print('lalu diikuti dengan 5 digit kode pembayaran')
        print('contoh 081563184352-55555')
        struk()
    elif bayar == 2:
        print('silahkan lakukan pembayaran ke rekening mandiri kami')
        print('720839214 A.N. Kasturia')
        print('lalu diikuti dengan 5 digit kode pembayaran')
        print('contoh 720839214-55555')
        struk()
    else:
        print('silahkan lakukan pembayaran ke rekening mandiri kami')
        print('081567878985 A.N. Katon')
        print('lalu diikuti dengan 5 digit kode pembayaran')
        print('contoh 081567878985-55555')
        struk()

# Fungsi Menu Awal
def menu_awal():
    print("Selamat Datang di Program Myulist".center(115))
    print("===============================================".center(115))
    print("Program ini merupakan program jual beli album lagu secara online".center(115))
    
    print("1. Genre")
    print("2. Penyanyi")
    print("3. Tahun")
    print("4. Keluar")

    pilihan = int(input("Masukkan pilihan anda: "))

    if pilihan == 1:
        genre()
        kembali_pembelian()
    elif pilihan == 2:
        penyanyi()
        kembali_pembelian()
    elif pilihan == 3:
        tahun()
        kembali_pembelian()
    elif pilihan == 4:
        print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI\n")
        pass
    else:
        menu_awal()

# Menjalankan program
menu_awal()
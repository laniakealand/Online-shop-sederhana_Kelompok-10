import pandas as pd
import csv
import os


# Define the shopping cart as a global variable
cart = []

# Load song data from CSV files
data_lagu_rock = pd.read_csv('data_rock.csv')
data_lagu_pop = pd.read_csv('data_pop.csv')
data_lagu_kpop = pd.read_csv('data_kpop.csv')


 
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
    else:
        print("INPUT SALAH")
        genre()


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
        menu_awal()


# Fungsi untuk menghapus item dari keranjang
def remove_from_cart():
    if not cart:
        print("Keranjang masih kosong!")
        input("Tekan ENTER untuk lanjut \n")
        menu_awal()
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
            menu_awal()


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
    menu_awal()


# Fungsi untuk melanjutkan pembayaran
def checkout():
    if not cart:
        print("Keranjang masih kosong!")
        input("Tekan ENTER untuk lanjut \n")
        menu_awal()
    else:
        print("== Struk Pembayaran ==")
        print("----------------------")
        total_price = sum(song['price'] for song in cart)
        for song in cart:
            print(f"{song['name']}: Rp{song['price']}")
        print(f"Total Harga: Rp{total_price}")
        name = input("Masukkan Nama Anda: ")
        address = input("Masukkan Alamat Rumah Anda: ")
        print(f"\nTerima kasih atas pembelian Anda, {name}!")
        print("Barang akan dikirim ke alamat berikut:")
        print(address)
        print("Silakan lakukan pembayaran.")
        input("Tekan ENTER untuk lanjut \n")
        # Reset the cart
        cart.clear()
        menu_awal()


# Fungsi Menu Awal
def menu_awal():
    print("Selamat Datang di Program Online Shop Sederhana".center(115))
    print("===============================================".center(115))
    print("Program ini merupakan program jual beli album lagu secara online".center(115))
    
    print("1. Genre")
    print("2. Penyanyi")
    print("3. Tahun")
    print("4. Keranjang")
    print("5. Hapus dari Keranjang")
    print("6. Lanjutkan Pembayaran")
    print("7. Keluar")

    pilihan = int(input("Masukkan pilihan anda: "))

    if pilihan == 1:
        genre()
    elif pilihan == 2:
        pass
    elif pilihan == 3:
        pass
    elif pilihan == 4:
        display_cart()
    elif pilihan == 5:
        remove_from_cart()
    elif pilihan == 6:
        checkout()
    elif pilihan == 7:
        print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI\n")
        pass
    else:
        menu_awal()


# Menjalankan program
menu_awal()

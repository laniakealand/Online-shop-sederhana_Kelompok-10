from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import csv
import os
data_lagu = pd.read_csv('data_lagu.csv')


def menu_awal():
    print("Selamat Datang di Program Online Shop Sederhana")
    print("===============================================")
    print("Program ini merupakan program jual beli album lagu secara online")
    
    print("1. Genre")
    print("2. Penyanyi")
    print("3. Tahun")

def Genre_Rock():
        print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
        pass

# Fungsi Display Item (Lagu)
def display_products(products):
    print("==Produk Tersedia==:")
    print("-------------------")
    for _, product in products.iterrows():
        print(f"{product['Genre']}, {product['Lagu']}, {product['Tahun']}, {product['Link']}: Rp{product['Harga']}")

# Fungsi Menambahkan Lagu ke Dalam My List
def add_to_cart(products, cart):
    display_products(products)
    product_name = input("Masukkan Item: ")
    quantity = int(input("Masukan Jumlah Item: "))

    # Mencari Item (Lagu) Dalam Display
    product = products[products['Lagu'] == product_name]
    if not product.empty:
        cart.append({'Genre': product['Genre'].values[0], 'Lagu': product['Lagu'].values[0], 'Tahun': product['Tahun'].values[0], 'Harga': product['Harga'].values[0], 'Link': product['Link'].values[0], 'quantity': quantity})
        print(f"{quantity} {product_name} dimasukkan dalam My List.")
    else:
        print("Lagu Tidak Ditemukan.")

# Fungsi Menampilkan Item di My List
def display_cart(cart):
    if len(cart) == 0:
        print("List Lagu Anda Kosong.")
    else:
        total = 0
        print("My List:")
        print("--------------")
        for item in cart:
            print(f"{item['Genre']}, {item['Lagu']}, {item['Tahun']}, {item['Harga']}, {item['Link']} : Rp{item['price']} x {item['quantity']}")
            total += item['price'] * item['quantity']
        print(f"Total: Rp{total}")

# Fungsi Menghapus Item Dalam My List
def remove_from_cart(cart):
    display_cart(cart)
    item_name = input("Masukkan Item yang Ingin Dihapus: ")

    for item in cart:
        if item['name'] == item_name:
            cart.remove(item)
            print(f"{item_name} dihapus dari My List.")
            return

    print("Lagu Tidak Ditemukan.")

# Fungsi Untuk Mengosongkan My List
def clear_cart(cart):
    cart.clear()
    print("My List Anda Dikosongkan.")

# Fungsi Import CSV Dengan Pandas
def import_products_from_csv(file_path):
    products = pd.read_csv(file_path)
    return products

#clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else clear)

def pilihan_menu():
        print("\nMenu:")
        print("1. Masukkan Item ke My List")
        print("2. Hapus Item dari My List")
        print("3. Kosongkan My List")
        print("4. Display My List")
        print("5. Keluar dari Program")
        print("6. Masuk ke menu pembayaran")
# Main program
def main():
    # Import Item pada CSV
    products = import_products_from_csv('data_lagu.csv')

    cart = []

    while True:
        print("\nMenu:")
        print("1. Masukkan Item ke My List")
        print("2. Hapus Item dari My List")
        print("3. Kosongkan My List")
        print("4. Display My List")
        print("5. Keluar dari Program")
        print("6. Masuk ke menu pembayaran")

        choice = input("Masukkan Pilihan Anda (1/2/3/4/5/6): ")

        if choice == '1':
            clear_screen()
            add_to_cart(products, cart)
        elif choice == '2':
            clear_screen()
            remove_from_cart(cart)
        elif choice == '3':
            clear_screen()
            clear_cart(cart)
        elif choice == '4':
            clear_screen()
            display_cart(cart)
        elif choice == '5':
            clear_screen()
            print("Terimakasih telah Menggunakan Program MyuList!")

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
        print(data_lagu)
        main()
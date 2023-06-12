from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import csv
import os

# Fungsi Display Item (Lagu)
def display_products(products):
    print("==Produk Tersedia==:")
    print("-------------------")
    for _, product in products.iterrows():
        print(f"{product['name']}: Rp{product['price']}")

# Fungsi Menambahkan Lagu ke Dalam My List
def add_to_cart(products, cart):
    display_products(products)
    product_name = input("Masukkan Item: ")
    quantity = int(input("Masukan Jumlah Item: "))

    # Mencari Item (Lagu) Dalam Display
    product = products[products['name'] == product_name]
    if not product.empty:
        cart.append({'name': product['name'].values[0], 'price': product['price'].values[0], 'quantity': quantity})
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
            print(f"{item['name']}: Rp{item['price']} x {item['quantity']}")
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

# Main program
def main():
    # Import Item pada CSV
    products = import_products_from_csv('laguPop.csv')

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
        elif choice == '6' :
            clear_screen()
            def buat_struk (nama_file, daftar_pembelian):
                c  = canvas.Canvas(nama_file, pagesize=letter)

                c.setFont("Helvetica", 12)
                c.drawString(100, 700, "Struk Pembayaran")

                y = 650
                total_harga = 0

                for lagu in daftar_pembelian:
                    nama_lagu = lagu['Nama Lagu']
                    artis = lagu['Artis']
                    harga = float(lagu['Harga'])

                    c.drawString(100, y, f"{nama_lagu} - {artis} (${harga})")
                    total_harga += harga
                    y -= 20

                c.drawString(100, y, "----------------------------------")
                y -= 20
                c.drawString(100, y, f"Total Harga: ${total_harga:.2f}")

                c.save()
                print("Terimakasih telah Menggunakan Program MyuList!")
    # Menentukan path file CSV
            file_csv = 'laguPop.csv'
            break
        else:
            print("Input Tidak Valid. Silakan Coba Lagi.")

# Run the program
if __name__== "__main__":
    main()
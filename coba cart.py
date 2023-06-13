import pandas as pd
import csv
import os
import random
import pdfkit

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

# Menu Opsi Pembayaran Merchandise
def metodebayar():
    print("Pilih Metode Pembayaran\n"
              "[1] Gopay\n"
              "[2] Bank Mandiri\n"
              "[3] Bank BNI\n")

    # Pengguna memilih metode pembayaran
    bayar = int(input('>>'))
    if bayar == 1:
        print('silahkan lakukan pembayaran ke akun gopay kami')
        print('081234567 A.N. Gabeta')
        print('lalu diikuti dengan 5 digit kode pembayaran')
        print('contoh 081234567-55555')
        struk()
    elif bayar == 2:
        print('silahkan lakukan pembayaran ke rekening mandiri kami')
        print('123456789 A.N. Kasturia')
        print('lalu diikuti dengan 5 digit kode pembayaran')
        print('contoh 123456789-55555')
        struk()
    else:
        print('silahkan lakukan pembayaran ke rekening BNI kami')
        print('123456789 A.N. Katon')
        print('lalu diikuti dengan 5 digit kode pembayaran')
        print('contoh 123456789-55555')
        struk()

#Total Pembelian:
def total(cart):
        global total

        total = 0
        print("My List:")
        print("--------------")
        for item in cart:
            print(f"{item['name']}: Rp{item['price']} x {item['quantity']}")
            total += item['price'] * item['quantity']
        print(f"Total: Rp{total}")
 
# Input Data User
def datapengguna():
    global nama
    global phone
    global rumah

    print('                 DATA USER                ')
    nama = input('Masukkan Nama Anda               : ')
    for name in nama:
        if name.isdigit():
            print("Tolong Masukan Dengan Huruf")
            datapengguna()
    phone = input('Masukkan No HP Anda             :+62 ')
    rumah = input('Masukkan Alamat Anda            : ')
    print()
    print('=========================================')
    print()
datapengguna()

# Struk Pembayaran
def struk():
    # kode pelunasan
    kode = random.randrange(55555, 77777, 10)
    print("Kode Pembayaran anda adalah", kode)
    print("Silahkan membayar ke No. Akun tersebut")
    print()
    while True:
        bayar = int(input("Masukan Kode Pelunasan: "))
        if bayar == kode:
            print("Pembayaran", bayar, "Berhasil. \n Hubungi Admin Jika Ada Kendala")
            break
        else:
            print("Maaf, Kode yang Dimasukkan Salah")

    # Template Struk
    output = f'''
    <html>
    <head> 
        <style>
            /* Add styling to the output */
            /* ... */

        </style>
    </head>
    <body>
        <h2>MYULIST RECAP</h2>
        <p>Nama                : {nama}</p>
        <p>Nomor HP            : {phone}</p>
        <p>Alamat              : {rumah}</p>
        <p>Kode Pembayaran     : {bayar}</p>
        <p>Total Pembelian     : {total}</p>
        <p>Terimakasih pesanan akan dikirim</p>
        <p>Apabila belum terkirim silakan hubungi Admin.</p>
    </body>
    </html>
    '''

    # Generate PDF from the HTML output
    pdfkit.from_string(output, 'struk.pdf')
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

        choice = input("Masukkan Pilihan Anda (1/2/3/4/5): ")

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
            lunas = input('Apakah Anda Ingin Melakukan Pembayaran? (Y/N) ')
            if lunas == "Y" or "y":
                total(cart)
                metodebayar()
                struk()
            else:
                main()
        elif choice == '5':
            clear_screen()
            print("Terimakasih telah Menggunakan Program MyuList!")
            break
        else:
            print("Input Tidak Valid. Silakan Coba Lagi.")

# Run the program
if __name__ == "__main__":
    main()
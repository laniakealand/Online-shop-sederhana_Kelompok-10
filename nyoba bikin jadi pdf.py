from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_receipt_pdf(customer_name, customer_address, cart):
    doc = SimpleDocTemplate("payment_receipt.pdf", pagesize=A4)

    # Menyiapkan konten struk
    styles = getSampleStyleSheet()
    content = []

    # Informasi pelanggan
    content.append(Paragraph(f"<b>Nama Pelanggan:</b> {customer_name}", styles['Normal']))
    content.append(Paragraph(f"<b>Alamat Pelanggan:</b> {customer_address}", styles['Normal']))
    content.append(Spacer(1, 12))

    # Daftar item
    table_data = [['No.', 'Item', 'Harga', 'Jumlah', 'Total']]
    for i, item in enumerate(cart, start=1):
        item_name = item['name']
        item_price = item['price']
        item_quantity = item['quantity']
        item_total = item_price * item_quantity
        table_data.append([str(i), item_name, str(item_price), str(item_quantity), str(item_total)])

    table_style = [('BACKGROUND', (0, 0), (-1, 0), '#CCCCCC'),
                   ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                   ('FONTSIZE', (0, 0), (-1, 0), 12),
                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                   ('BACKGROUND', (0, 1), (-1, -1), '#FFFFFF'),
                   ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                   ('FONTSIZE', (0, 1), (-1, -1), 10),
                   ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
                   ('GRID', (0, 0), (-1, -1), 1, '#000000')]

    from reportlab.lib import colors
    table = Table(table_data, style=table_style)
    content.append(table)
    content.append(Spacer(1, 24))

    # Total pembayaran
    total = sum(item['price'] * item['quantity'] for item in cart)
    content.append(Paragraph(f"<b>Total:</b> {total}", styles['Normal']))

    # Membuat struk PDF
    doc.build(content)

    print("Struk pembayaran berhasil dibuat.")
def main():
    # Import Item pada CSV
    products = import_products_from_csv('laguPop.csv')

    cart = []

    print("Selamat Datang di Program MyuList!")

    customer_name = input("Masukkan Nama Anda: ")
    customer_address = input("Masukkan Alamat Anda: ")

    while True:
        print("\nMenu:")
        print("1. Masukkan Item ke My List")
        print("2. Hapus Item dari My List")
        print("3. Kosongkan My List")
        print("4. Display My List")
        print("5. Cetak Struk Pembayaran")
        print("6. Keluar dari Program")

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
            create_receipt_pdf(customer_name, customer_address, cart)
        elif choice == '6':
            clear_screen()
            print("Terimakasih telah Menggunakan Program MyuList!")
            break
        else:
            print("Input Tidak Valid. Silakan Coba Lagi.")

# Run the program
if __name__ == "__main__":
    main()
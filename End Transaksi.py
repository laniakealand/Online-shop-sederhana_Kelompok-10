 
def tampilkanBarang():
    no = 1
    print("")
    print("")
    print("======== DESKRIPSI ALBUM =========")
    for b in barang:
        print("=================")
        print("No :",no)
        print("Nama : ",b['artis'])
        print("Merek : ",b['judul'])
        print("Type : ",b['tahun'])
        print("Harga : Rp.",b['harga'])
        print("=================")
        no += 1
    print("")
    print("No "+str(no)+" : Keluar")
    print("")
    beliBarang(no)
 
def beliBarang(no):
    plh_brg = inputAngka("Pilih Nomor Barang : ")
    if(plh_brg == no):
        print("")
    else:
        b = barang[plh_brg-1]
        print("========= Beli Barang ========")
        print("Artis : ",b['artis'])
        print("Judul : ",b['judul'])
        print("Tahun : ",b['tahun'])
        print("Harga : Rp.",b['harga'])
        print("==============================")
        print("1.Beli")
        print("2.Kembali")
        plh_mn = inputAngka("Pilih Nomor Barang : ")
        if(plh_mn == 1):
            trans = {
                "barang":b,
                "total":b['harga'],
                "batas_waktu":datetime.datetime.now()+timedelta(minutes=batas_pembayaran_transaksi),
                "status":"Belum Dibayar"
                }
                # pelanggan[index]['saldo'] -= b['harga']
                print("==============================")
                print("Anda Sudah Membeli : ")
                print("Nama : ",b['nama'])
                print("Dengan Harga : Rp.",b['harga'])
                print("Silahkan Bayar Tagihan Sebelum ",trans['batas_waktu'])
                print("==============================")
                pelanggan[index]['transaksi'].append(trans)
        else :
            return to HomePage
        print("")
        print("")
 
def tampilkanTransaksi():
    no = 1
    print("")
    print("")
    print("======== DATA TRANSAKSI =========")
    for t in pelanggan[index]['transaksi']:
        print("=================")
        print("No :",no)
        print("Artis : ",t['barang']['artis'])
        print("Judul : ",t['barang']['judul'])
        print("Tahun : ",t['barang']['tahun'])
        print("Total : Rp.",t['total'])
        print("Status : ",t['status'])
        print("Batas Waktu : ",t['batas_waktu'])
        print("=================")
        no += 1
    print("")
    print("No "+str(no)+" : Keluar")
    print("")
    bayarTransaksi(no)
 
def bayarTransaksi(no):
    plh_trans = inputAngka("Pilih Nomor Transaksi : ")
    print("")
    print("")
    if(plh_trans == no):
        print("")
    else:
        trans = pelanggan[index]['transaksi'][(plh_trans - 1)]
        if(trans['batas_waktu'] < datetime.datetime.now()):
            print("")
            print("")
            print("====================")
            print("Transaksi Sudah Melebihi Batas Yang Di Tentukan Maka Pembayaran Dibatalkan")
            print("====================")
        elif(trans['status'] == "Sudah Dibayar"):
            print("====================")
            print("Transaksi Sudah Di Bayar")
            print("====================")
        else:
            print("====================")
            print("Berhasil Membayar Transaksi Sebesar : ",trans['total'])
            pelanggan[index]['saldo'] -= trans['total']
            print("====================")
    print("")
    print("")
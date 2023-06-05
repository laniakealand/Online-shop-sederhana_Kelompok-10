def menu_awal():
    print("Selamat Datang di Program Online Shop Sederhana")
    print("===============================================")
    print("Program ini merupakan program jual beli album lagu secara online")
    
    print("1. Genre")
    print("2. Penyanyi")
    print("3. Tahun")
    
print("Selamat Datang di Program Online Shop Sederhana")
print("===============================================")
print("Program ini merupakan program jual beli album lagu secara online")
    
print("1. Genre")
print("2. Penyanyi")
print("3. Tahun")

pilihan_1 = input ("Masukkan filter yang ingin anda pilih: ")
if pilihan_1 == "1":
    
#menampilkan info program
    def menu_genre():
        print("Selamat Datang di Program Online Shop Sederhana")
        print("===============================================")
        print("Program ini merupakan program jual beli album lagu secara online")
        print("Pilihan genre lagu yang ditawarkan pada program ini berupa lagu Rock, Pop dan K-Pop.")

#menampilkan info genre lagu
        print("Informasi Genre Lagu")
        print("1. Rock")
        print("2. Pop")
        print("3. K-Pop")
        print("4. Keluar")
    
    print("Selamat Datang di Program Online Shop Sederhana")
    print("===============================================")
    print("Program ini merupakan program jual beli album lagu secara online")
    print("Pilihan genre lagu yang ditawarkan pada program ini berupa lagu Rock, Pop dan K-Pop.")

#menampilkan info genre lagu
    print("Informasi Genre Lagu")
    print("1. Rock")
    print("2. Pop")
    print("3. K-Pop")
    print("4. Keluar")

#menampilkan pilihan lagu
    pilihan_2 = input("Pilih genre lagu (1-4): ")
    if pilihan_2 == "1":
        print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
        from List_Lagu import Rock
        print (Rock)
        print("1. Artis")
        print("2. Judul")
        print("3. Tahun")
        print("4. Keluar")
        pilihan_3 = input("Masukkan filter yang ingin anda pilih: ")
        if pilihan_3 == "1":
            pencarian_artis = input("Masukkan artis yang ingin anda cari: ")
            for lagu in Rock:
                if lagu['artis'] == pencarian_artis:
                    print("Artis:", lagu['artis'])
                    print("Judul:", lagu['judul'])
                    print("Tahun:", lagu['tahun'])
                else:
                    ("Maaf lagu yang anda cari tidak tersedia")
                    pilihan_4 = input("Apakah anda ingin kembali ke menu awal? (Ya/Tidak) ")
                    if pilihan_4.lower() == "ya":
                        menu_awal()
                    else:
                        print("Terimakasih telah mengunjungi informasi genre lagu.")
        elif pilihan_3 == "2":
            pencarian_judul = input("Masukkan judul yang ingin anda cari: ")
            for lagu in Rock:
                if lagu['judul'] == pencarian_judul:
                    print("Artis:", lagu['artis'])
                    print("Judul:", lagu['judul'])
                    print("Tahun:", lagu['tahun'])
                else:
                    ("Maaf lagu yang anda cari tidak tersedia")
                    pilihan_4 = input("Apakah anda ingin kembali ke menu awal? (Ya/Tidak) ")
                    if pilihan_4.lower() == "ya":
                        menu_awal()
                    else:
                        print("Terimakasih telah mengunjungi informasi genre lagu.")
        elif pilihan_3 == "3":
            pencarian_tahun = input("Masukkan tahun yang ingin anda cari: ")
            for lagu in Rock:
                if lagu['tahun'] == pencarian_tahun:
                    print("Artis:", lagu['artis'])
                    print("Judul:", lagu['judul'])
                    print("Tahun:", lagu['tahun'])
                else:
                    ("Maaf lagu yang anda cari tidak tersedia")
                    pilihan_4 = input("Apakah anda ingin kembali ke menu awal? (Ya/Tidak) ")
                    if pilihan_4.lower() == "ya":
                        menu_awal()
                    else:
                        print("Terimakasih telah mengunjungi informasi genre lagu.")
        elif pilihan_3 == "4":
            print("Terimakasih telah mengunjungi genre lagu rock.")
        else:
             print("Maaf pilihan yang anda masukkan tidak tersedia.")
             pilihan_4 = input("Apakah anda ingin kembali ke menu awal? (Ya/Tidak) ")
             if pilihan_4.lower() == "ya":
                menu_awal()
             else:
                print("Terimakasih telah mengunjungi informasi genre lagu.")
    elif pilihan_2 == "2":
        print("Genre musik pop adalah salah satu genre musik yang terkenal. Bahkan genre musik pop bisa dibilang sebagai aliran musik paling populer dan paling banyak dinyanyikan oleh penyanyi dan band di seluruh dunia.")
        import List_Lagu
        tahun_pencarian = input("Masukkan tahun yang ingin anda cari: ")

        for lagu in List_Lagu.Pop:
            if lagu[''] == tahun_pencarian:
                print("Artis:", lagu['artis'])
                print("Judul:", lagu['judul'])
                print("Link:", lagu['link'])
    elif pilihan_2 == "3":
        print("Genre musik k-pop adalah genre musik populer yang berasal dari Korea Selatan. Lagu-lagu K-pop banyak dipengaruhi oleh berbagai genre musik, seperti hip-hop, electronic dance, jazz, dan rock.")
        import List_Lagu
        tahun_pencarian = input("Masukkan tahun yang ingin Anda cari: ")

        for lagu in List_Lagu.Kpop:
            if lagu['tahun'] == tahun_pencarian:
                print("Artis:", lagu['artis'])
                print("Judul:", lagu['judul'])
                print("Link:", lagu['link'])
    elif pilihan_2 == "4":
        print("Terimakasih telah mengunjungi informasi genre lagu.")
    else:
        print("Maaf pilihan yang anda masukkan tidak tersedia.")
        pilihan_3 = input("Apakah anda ingin kembali ke menu awal? (Ya/Tidak) ")
        if pilihan_3.lower() == "ya":
            menu_genre()
        else:
            print("Terimakasih telah mengunjungi informasi genre lagu.")

elif pilihan_1 == "2":
    def menu_genre():
        print("Selamat Datang di Program Online Shop Sederhana")
        print("===============================================")
        print("Program ini merupakan program jual beli album lagu secara online")
        print("Pilihan berdasarkan penyanyi yang ditawarkan pada program ini berupa Boyband, Girlband dan Single.")

#menampilkan info genre lagu
        print("Informasi Penyanyi")
        print("1. Boyband")
        print("2. Girlband")
        print("3. Single")
        print("4. Keluar")
    
    print("Selamat Datang di Program Online Shop Sederhana")
    print("===============================================")
    print("Program ini merupakan program jual beli album lagu secara online")
    print("Pilihan berdasarkan penyanyi yang ditawarkan pada program ini berupa Boyband, Girlband dan Single.")

#menampilkan info genre lagu
    print("Informasi Penyanyi")
    print("1. Boyband")
    print("2. Girlband")
    print("3. Single")
    print("4. Keluar")

#menampilkan pilihan lagu
    pilihan = input("Pilih penyanyi (1-4): ")
    if pilihan == "1":
        print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
        import List_Lagu
        tahun_pencarian = input("Masukkan tahun yang ingin Anda cari: ")

        for lagu in List_Lagu.Rock:
            if lagu['tahun'] == tahun_pencarian:
                print("Artis:", lagu['artis'])
                print("Judul:", lagu['judul'])
    elif pilihan == "2":
        print("Genre musik pop adalah salah satu genre musik yang terkenal. Bahkan genre musik pop bisa dibilang sebagai aliran musik paling populer dan paling banyak dinyanyikan oleh penyanyi dan band di seluruh dunia.")
        import List_Lagu
        tahun_pencarian = input("Masukkan tahun yang ingin Anda cari: ")

        for lagu in List_Lagu.Pop:
            if lagu['tahun'] == tahun_pencarian:
                print("Artis:", lagu['artis'])
                print("Judul:", lagu['judul'])
                print("Link:", lagu['link'])
    elif pilihan == "3":
        print("Genre musik k-pop adalah genre musik populer yang berasal dari Korea Selatan. Lagu-lagu K-pop banyak dipengaruhi oleh berbagai genre musik, seperti hip-hop, electronic dance, jazz, dan rock.")
        import List_Lagu
        tahun_pencarian = input("Masukkan tahun yang ingin Anda cari: ")

        for lagu in List_Lagu.Kpop:
            if lagu['tahun'] == tahun_pencarian:
                print("Artis:", lagu['artis'])
                print("Judul:", lagu['judul'])
                print("Link:", lagu['link'])
    elif pilihan == "4":
        print("Terimakasih telah mengunjungi informasi genre lagu.")
    else:
        print("Maaf pilihan yang anda masukkan tidak tersedia.")
        pilihan_2 = input("Apakah anda ingin kembali ke menu awal? (Ya/Tidak) ")
        if pilihan_2.lower() == "ya":
            menu_genre()
        else:
            print("Terimakasih telah mengunjungi informasi genre lagu.")
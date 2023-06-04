#menampilkan info program
print("Selamat Datang di Program Online Shop Sederhana")
print("===============================================")
print("Program ini merupakan program jual beli album lagu secara online")
print("Pilihan genre lagu yang ditawarkan pada program ini berupa lagu Rock, Pop dan K-Pop.")

#menampilkan info genre lagu
while True:
    print("Informasi Genre Lagu")
    print("1. Rock")
    print("2. Pop")
    print("3. K-Pop")
    print("4. Keluar")

pilihan = input("Pilih genre lagu (1-4): ")
if pilihan == "1":
    print("Genre musik rock adalah suatu genre musik populer yang mulai tumbuh sejak era 50an. Musik rock terbentuk karena pengaruh musik R&B dan country di era 40an.")
elif pilihan == "2":
    print("Genre musik pop adalah salah satu genre musik yang terkenal. Bahkan genre musik pop bisa dibilang sebagai aliran musik paling populer dan paling banyak dinyanyikan oleh penyanyi dan band di seluruh dunia.")
elif pilihan == "3":
    print("Genre musik k-pop adalah genre musik populer yang berasal dari Korea Selatan. Lagu-lagu K-pop banyak dipengaruhi oleh berbagai genre musik, seperti hip-hop, electronic dance, jazz, dan rock.")
elif pilihan == "4":
    print("Terimakasih telah mengunjungi informasi genre lagu.")

#menampilkan pilihan lagu
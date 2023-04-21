def cetak(datasf,i):
# mencetak data gadget dengan indeks i dalam datasf
    print("Nama            : ",datasf[i][1])
    print("Deskripsi       : ",datasf[i][2])
    print("Jumlah          : ",datasf[i][3], "buah")
    print("Rarity          : ",datasf[i][4])
    print("Tahun Ditemukan : ",datasf[i][5])
    print()

def caritahun(datasf):
# menerima data gadget dan memberikan gadget dengan tahun yg bersesuaian
# Akses : Admin, User
    findtahun = int(input("Masukkan tahun: ")) # tahun yang di-input pasti valid (>0)
    if (0<findtahun<9999):
        kategori = input("Masukkan kategori: ") # kategori yang di-input pasti valid (=,<,>,>=,<=)
        print()
        print("Hasil pencarian:")
        print()
        valid_kategori = ["=",">","<",">=","<="]
        found = False
        if kategori in valid_kategori:
            for i in range(1,len(datasf)):
                if (kategori == "="):
                    if (int(datasf[i][5]) == findtahun):
                        found = True
                        cetak(datasf,i)
                elif (kategori == "<"):
                    if (int(datasf[i][5]) < findtahun):
                        found = True
                        cetak(datasf,i)
                elif (kategori == ">"):
                    if (int(datasf[i][5]) > findtahun):
                        found = True
                        cetak(datasf,i)
                elif (kategori == ">="):
                    if (int(datasf[i][5]) >= findtahun):
                        found = True
                        cetak(datasf,i)
                elif (kategori == "<="):
                    if (int(datasf[i][5]) <= findtahun):
                        found = True
                        cetak(datasf,i)
            if found == False:
                print("Tidak ada gadget dengan Tahun Ditemukan", kategori, findtahun)
        else:
            print("Kategori tidak valid, masukkan harus (=,<,>,>=,<=)")
    else:
        print()
        print("Tahun tidak valid, masukkan harus angka > 0 kurang dari 9999")
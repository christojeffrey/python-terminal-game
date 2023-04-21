def carirarity(datasf):
#menerima array data gadget, dan melakukan prosedur mencari rarity
# Akses : Admin, User
    findrarity = input("Masukkan rarity: ") # jenis rarity yang di-input pasti valid (C,B,A,S)
    print()
    found = False
    for i in range(len(datasf)):
        if datasf[i][4] == findrarity:
            found = True
            print("Nama            : ",datasf[i][1])
            print("Deskripsi       : ",datasf[i][2])
            print("Jumlah          : ",datasf[i][3], "buah")
            print("Rarity          : ",datasf[i][4])
            print("Tahun Ditemukan : ",datasf[i][5])
            print()
    if found == False:
        print("Tidak ada gadget dengan rarity",findrarity)
def tambahitem(datasf,datasg):
# prosedur menerima data gadget dan data consumable, lalu menambahnya sesuai ketentuan. lalu mereturn data yg sudah di modifikasi
# Akses : Admin
    idx = input("Masukan ID               : ")
    valid_rarity = ["C","B","A","S"]
    found = False
    if (idx[0] == 'G') and (len(idx)>1):
        for i in range(len(datasf)):
            if idx == datasf[i][0]:
                found = True
                print()
                print("Gagal menambahkan item karena ID sudah ada")
        if found == False:
            nama    = input("Masukan Nama             : ")
            des     = input("Masukan Deskripsi        : ")
            jumlah  = int(input("Masukan Jumlah           : "))
            if jumlah > 0:
                rarity  = input("Masukan Rarity           : ")
                if rarity in valid_rarity:
                    tahun   = int(input("Masukan Tahun Ditemukan  : "))
                    if tahun > 0:
                        newgadget = [idx,nama,des,jumlah,rarity,tahun]
                        datasf.append(newgadget)
                        print()
                        print("Item telah berhasil ditambahkan ke database")
                    else:
                        print()
                        print("Input tahun ditemukan tidak valid!")
                else:
                    print()
                    print("Input rarity tidak valid!")
            else:
                print()
                print("Input jumlah tidak valid!")
    elif (idx[0] == 'C') and (len(idx)>1):
        for i in range(len(datasg)):
            if idx == datasg[i][0]:
                found = True
                print()
                print("Gagal menambahkan item karena ID sudah ada")
        if found == False:
            nama    = input("Masukan Nama             : ")
            des     = input("Masukan Deskripsi        : ")
            jumlah  = int(input("Masukan Jumlah           : "))
            if jumlah > 0:
                rarity  = input("Masukan Rarity           : ")
                if rarity in valid_rarity:
                    newgadget = [idx,nama,des,jumlah,rarity]
                    datasg.append(newgadget)
                    print()
                    print("Item telah berhasil ditambahkan ke database")
                else:
                    print()
                    print("Input rarity tidak valid!")
            else:
                print()
                print("Input jumlah tidak valid!")
    else:
        print()
        print("Gagal menambahkan item karena ID tidak valid")
    return datasf, datasg
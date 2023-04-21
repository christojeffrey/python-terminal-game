def hapusitem(datasf, datasg):
# prosedur menerima data gadget dan data consumable, lalu menghapusnya sesuai ketentuan. lalu me return data yang sudah di modifikasi
# Akses : Admin
# datasf = data gadget
# datasg = data consumable
    idx = input("Masukan ID item : ")
    option = "N"
    found = False
    if (idx[0] == 'G'):
        for i in range(len(datasf)):
            if (idx == datasf[i][0]):
                found = True
                print("Apakah anda yakin ingin menghapus", datasf[i][1], "(Y/N)? ")
                option = input()
                if option == "Y":
                    datasf.pop(i)
                    print()
                    print("Item telah berhasil dihapus dari database")
                else:
                    print()
                    print("Item tidak jadi dihapus")
                break
        if found == False:
            print()
            print("Tidak ada item dengan ID tersebut")
    elif (idx[0] == 'C'):
        for i in range(len(datasg)):
            if datasg[i][0] == idx :
                print(datasg[i][0])
                found = True
                print("Apakah anda yakin ingin menghapus", datasg[i][1], "(Y/N)? ")
                option = input()
                if option == "Y":
                    datasg.pop(i)
                    print()
                    print("Item telah berhasil dihapus dari database")
                else:
                    print()
                    print("Item tidak jadi dihapus")
                break
        if found == False:
            print()
            print("Tidak ada item dengan ID tersebut")
    else:
        print()
        print("Gagal menghapus item karena ID tidak valid")
    return datasf, datasg
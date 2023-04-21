import os
def arrtocsv(namaarray,lokasifile):
# sebuah prosedur
# menerima array lalu menuliskannya di namafile. namafile boleh baru, boleh sudah ada, jika sudah ada maka akan di overwrite
    stringdata = ""
    for b in range (len(namaarray)):
        for k in range(len(namaarray[0])):
            if (k == len(namaarray[0])-1):
                stringdata +=str(namaarray[b][k]) + "\n"
            else:
                stringdata +=str(namaarray[b][k]) + ";"
    data = open(lokasifile,"w")
    data.write(stringdata)
    data.close()
# end of def arrtocsv

def save(arr_user, arr_gadget, arr_consumable, arr_consumable_history, arr_gadget_borrow_history, arr_gadget_return_history):
    namafolder = input("masukkan nama folder tempat file akan di save = ")
    lokasi = carifolder(namafolder)
    if lokasi == "":
        os.mkdir(namafolder)
        lokasi = namafolder
    arrtocsv(arr_user, lokasi + "/user.csv")
    arrtocsv(arr_gadget, lokasi + "/gadget.csv")
    arrtocsv(arr_consumable,lokasi + "/consumable.csv")
    arrtocsv(arr_consumable_history, lokasi +"/consumable_history.csv")
    arrtocsv(arr_gadget_borrow_history, lokasi + "/gadget_borrow_history.csv")
    arrtocsv(arr_gadget_return_history, lokasi + "/gadget_return_history.csv")

def carifolder(namafolder):
    folder = namafolder
    lokasi = ""
    for root, dirs, files in os.walk("..", topdown=True):
       for name in dirs:
        if (name == folder):
            # print("ketemu")
            lokasi = os.path.join(root, name)
    return lokasi
# end of all function




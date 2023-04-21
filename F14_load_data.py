
def jum_baris(s):
    return s.count("\n")

def jum_kolom(s):
    return int(1+(s.count(";")/ jum_baris(s)))

def csvtoarr(namafile):
    # sebuah fungsi
    # menerima file csv, trus di ubah jadi array. FILE NYA HARUS UDAH ADA
    data = open(namafile)
    stringdata = data.read()
    data.close()
    # kalo bagian belakangnya bukan slash n, akan ditambahin
    if not(stringdata.endswith("\n")):
        #print("ini ke run")
        stringdata += "\n"

    arraydata = [["" for k in range (jum_kolom(stringdata))] for b in range (jum_baris(stringdata))]
    start = 0
    end = -1
    for b in range(jum_baris(stringdata)):
        for k in range(jum_kolom(stringdata)):
            start = end +1
            if (k == jum_kolom(stringdata)-1):
                end = stringdata[start:len(stringdata)].find("\n") + end + 1
            else:
                end = stringdata[start:len(stringdata)].find(";") + end + 1
            arraydata[b][k] = stringdata[start:end]
    return arraydata
 # end of def csvtoarr

def load(namafolder):
	#me-load file2 yang ada di dalam folder tersebut,
	#me return array data(5 biji)
	arr_user = csvtoarr(namafolder + "/user.csv")
	arr_gadget = csvtoarr(namafolder + "/gadget.csv")
	arr_consumable = csvtoarr(namafolder + "/consumable.csv")
	arr_consumable_history = csvtoarr(namafolder +"/consumable_history.csv")
	arr_gadget_borrow_history = csvtoarr(namafolder + "/gadget_borrow_history.csv")
	arr_gadget_return_history = csvtoarr(namafolder + "/gadget_return_history.csv")
	return arr_user, arr_gadget, arr_consumable, arr_consumable_history, arr_gadget_borrow_history, arr_gadget_return_history

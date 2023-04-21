import validasitanggal
def minta(role,username,arrc,arrch): #arrc = arrconsumable, arrch = array consumable history
	if role == "user":
		ID = input("masukkan ID item consumable = ")
		if ID[0] != "C":
			print("ID tidak valid")
			return arrc, arrch

		datake = -1
		ketemu = False
		for line in arrc:
			datake = datake + 1
			if line[0] == ID:
				ketemu = True
				stok = int(line[3])
				break
		if not(ketemu):
			print("tidak ada item consumable dengan ID tersebut")
		else:
			while True:
				jum = input("masukkan jumlah = ")
				if jum.isdigit():
					if int(jum) <= stok:
						jum = int(jum)
						break
					else:
						print("stok tidak cukup.(hanya ada", stok,")")
				else:
					print("input tidak valid, harus angka dan lebih dari 0")
			while True:
				tgl = input("masukkan tanggal permintaan = ")
				if not(validasitanggal.validasitanggal(tgl)):
					print("tanggal tidak valid")
				else:
					break
			arrc[datake][3] = int(arrc[datake][3]) - jum
			arrch.append([len(arrch), username,ID,tgl,jum])
	else: #rolenya admin, tidak boleh
		print("hanya untuk user")
	return arrc, arrch
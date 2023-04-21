import validasitanggal
def pinjam(akses,username,arrg,arrpg): #arrg = arr gadget, arrpg = arr pinjam gadget
#menerima 4 parameter, dan memberikan arrg dan arrpg yang sudah diubah sesuai masukan pengguna
	if akses == "user":
		ID = input("masukkan ID item = ")
		ketemu = False
		for line in arrg:
			if line[0] == ID:
				ketemu = True
				break # ID yg bersesuaian sudah ketemu, jadi gk perlu cari lagi
		if ketemu == False:
			print("gadget dengan ID tersebut tidak ada")
			return arrg,arrpg
		tgl = input("masukkan tanggal peminjaman = ")
		if not(validasitanggal.validasitanggal(tgl)):#validasi tanggal
			print("tanggal tidak valid")
			return arrg, arrpg
		jum =input("masukkan jumlah peminjaman = ")
		if not(jum.isdigit()):
			print("jumlah tidak valid")
			return arrg, arrpg
		jum = int(jum)
		#cek dulu, apakah dia pernah pinjam gadget yg sama
		spj = False #spj = sedang pinjam
		for line in arrpg:
			if line[2] == ID and line[1] == username and line[5] == "False":
				spj = True
				print("kamu sedang meminjam barang yg sama, jadi tidak boleh pinjam lagi")
				break
		if spj == False:
			for line in arrg[1:]:
				if line[0] == ID:
					if int(line[3]) < jum:
						print("jumlah peminjaman melebihi jumlah yg ada(hanya ada", line[3],")")
					else: # item bisa dipinjam
						line[3] = int(line[3]) - jum
						arrpg.append([len(arrpg),username,ID,tgl,jum,"False"])
	else:
		print("hanya user yg boleh meminjam!")
	return arrg, arrpg
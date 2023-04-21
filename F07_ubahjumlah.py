def ubahjumlah(akses, arrc, arrg):
	if akses == "admin":
		ID = input("masukkan ID = ")
		jumlah = int(input("masukkan jumlah = "))
		ketemu = False
		if ID[0] == "C":
			for line in arrc:
				if line[0] == ID:
					ketemu = True
					if int(line[3]) + jumlah > 0:
						line[3] = int(line[3]) + jumlah
						if jumlah > 0:
							print(jumlah, line[1],"berhasil ditambahkan. Jumlah sekarang", line[3])
						else:
							print(jumlah, line[1],"berhasil dibuang. Jumlah sekarang", line[3])
					else:
						print(jumlah, line[1], "gagal dibuang. Jumlah sekarang", line[3], "(kurang dari",-jumlah,")")
					break
		else:
			for line in arrg:
				if line[0] == ID:
					ketemu = True
					if int(line[3]) + jumlah > 0:
						line[3] = int(line[3]) + jumlah
						if jumlah > 0:
							print(jumlah, line[1],"berhasil ditambahkan. Jumlah sekarang", line[3])
						else:
							print(jumlah, line[1],"berhasil dibuang. Jumlah sekarang", line[3])
					else:
						print(jumlah, line[1], "gagal dibuang. Jumlah sekarang", line[3], "(kurang dari",-jumlah,")")
					break
		if not(ketemu):
			print("Tidak ada item dengan ID tersebut!")
	else:
		print("hanya admin yg boleh mengubah jumlah data!")
	return arrc, arrg
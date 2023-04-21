import validasitanggal
def kembalikan(role,username,arrbh, arrrh,arrg): #arrbh = array borrow history, arrrh array return history, arrg = array gadget
	if role =="user":
		nomor = 0
		note = ["" for i in range(len(arrbh))] # untuk mencatat ID data peminjaman, penomoran mulai dari satu
		for line in arrbh:
		#keep in mind, seseorang tidak bisa meminjam gadget yg sama ketika sedang meminjam gaddget tersebut, jadi data di line gamungkin dobel
			if line[1] == username and line[5] == "False":
				nomor = nomor + 1
				print(str(nomor) + "." + gadgetname(arrg,line[2]))
				note[nomor] = int(line[0])
		if nomor == 0:
			print("kamu tidak meminjam apa2")
		else:
			while True: #validasi variabel pilihan dulu
				pilihan = (input("pilih nomor peminjaman yg mau dikembalikan = "))
				if pilihan.isdigit():
					pilihan = int(pilihan)
					if pilihan <= nomor:
						break
					else:
						print("angka yg dimasukkan tidak benar, harus sesuai list diatas")
				else:
					print("inputan bkn angka. masukkan angka")
			while True:
				tgl = input("masukkan tanggal pengembalian = ")
				if not(validasitanggal.validasitanggal(tgl)):
					print("tanggal tidak valid")
				else:
					break

			print("jumlah", gadgetname(arrg,arrbh[note[pilihan]][2]),"yang kamu pinjam sebanyak",arrbh[note[pilihan]][4])
			while True:
				parsial = input("masukkan jumlah yg ingin dikembalikan = ")
				if not(parsial.isdigit()):
					print("imput tidak valid")
				elif int(parsial) > int(arrbh[note[pilihan]][4]):
					print("jumlah yg dikembalikan melebihi jumlah yang kamu pinjam, ulangi")
				else:
					parsial = int(parsial)
					break
			#sekarang waktunya mengubah data arrbh dan arrrh
			#tambah data di arrrh
			arrrh.append([len(arrrh),str(note[pilihan]),tgl,int(arrbh[note[pilihan]][4])])
			#ubah data di arrbh. kalo yg dikembaliin sebagian, seakan2 dia balikin semua, lalu pinjam lagi.
			arrbh[note[pilihan]][5] = "True"
			if parsial < int(arrbh[note[pilihan]][4]): # kalo dia gk ngembalikin semuanya,
				arrbh.append([len(arrbh), username,arrbh[note[pilihan]][2],arrbh[note[pilihan]][3],(int(arrbh[note[pilihan]][4]) - parsial),"False"])
			#mengubah data di arrgadget, karena sudah dikembalikan jadi nambah lagi
			for line in arrg:
				if line[0] == arrbh[note[pilihan]][2]:
					line[3] = int(line[3]) + parsial
	else: #dia bukan user, dia admin
		print("hanya boleh untuk user, bkn untuk admin")
	return arrbh, arrrh,arrg
def gadgetname(arrg,ID): 
#menerima id gadget, dan memberikan nama gadget dengan ID tersebut
	for line in arrg:
		if line[0] == ID:
			return line[1]

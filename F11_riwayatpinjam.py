import sortbydate
def riwayatpinjam(role, arrbh,arrg): #arrbh = array borrow history
	if role == "admin":
		count = 0
		for line in sortbydate.sortbydate(arrbh[1:],3):
			if count % 5 == 0 and count != 0:
				while True:
					yorn = input("mau print data lagi?(y/n)")
					if yorn == "y":
						print("ID Peminjaman 		: ", line[0])
						print("Nama Pengambil		: ", line[1])
						print("Nama Gadget 		: ", gadgetname(arrg,line[2]))
						print("Tanggal peminjaman 	: ",line[3])
						print("Jumlah 			: ",line[4])
						print("")
						count = count + 1
						break
					elif yorn == "n":
						break
					else:
						print("input bkn (y/n). ulangi lagi")
				if yorn == "n":
					break
			else:
				if line[5] == "False":
					print("ID Peminjaman 		: ", line[0])
					print("Nama Pengambil		: ", line[1])
					print("Nama Gadget 		: ", gadgetname(arrg,line[2]))
					print("Tanggal peminjaman 	: ",line[3])
					print("Jumlah 			: ",line[4])
					print("")
					count = count + 1
		print("data selesai")
	else:
		print("hanya boleh admin!")
def gadgetname(arrg,ID): 
#menerima id gadget, dan memberikan nama gadget dengan ID tersebut
	for line in arrg:
		if line[0] == ID:
			return line[1]
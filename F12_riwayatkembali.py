import sortbydate
def riwayatkembali(role, arrrh,arrbh,arrg): #arrbh = array borrow history, arrrh = array return history
	if role == "admin":
		count = 0
		for line in sortbydate.sortbydate(arrrh[1:],2):
			if count % 5 == 0 and count != 0:
				while True:
					yorn = input("mau print data lagi?(y/n)")
					if yorn == "y":
						print("ID Peminjaman 		: ", line[0])
						print("Nama Pengambil		: ", arrbh[int(line[1])][1])
						print("Nama Gadget 		: ", gadgetname(arrg,arrbh[int(line[1])][2]))
						print("Tanggal peminjaman 	: ",line[2])
						print("Jumlah 		:", line[3])
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
				print("ID Peminjaman 		: ", line[0])
				print("Nama Pengambil		: ", arrbh[int(line[1])][1])
				print("Nama Gadget 		: ", gadgetname(arrg,arrbh[int(line[1])][2]))
				print("Tanggal peminjaman 	: ",line[2])
				print("Jumlah 		:", line[3])
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
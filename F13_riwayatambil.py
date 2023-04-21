import sortbydate
def riwayatambil(role, arrch,arrc): #arrch = array consumable history, arrc = arr consumable
	if role == "admin":
		count = 0
		for line in sortbydate.sortbydate(arrch[1:],3):
			if count % 5 == 0 and count != 0:
				while True:
					yorn = input("mau print data lagi?(y/n)")
					if yorn == "y":
						print("ID Peminjaman 		: ", line[0])
						print("Nama Pengambil		: ", line[1])
						print("Nama Consumable 	: ", consumablename(arrc,line[2]))
						print("Tanggal Pengambilan 	: ", line[3])
						print("Jumlah 			: ", line[4])
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
				print("Nama Pengambil		: ", line[1])
				print("Nama Consumable 	: ", consumablename(arrc,line[2]))
				print("Tanggal Pengambilan 	: ", line[3])
				print("Jumlah 			: ", line[4])
				print("")
				count = count + 1
		print("data selesai")
	else:
		print("hanya boleh admin!")
def consumablename(arrc,ID): 
#menerima id gadget, dan memberikan nama gadget dengan ID tersebut
	for line in arrc:
		if line[0] == ID:
			return line[1]
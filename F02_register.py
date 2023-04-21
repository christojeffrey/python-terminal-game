import FB01_hashing
def register(arr,role):
	#menerima array user dan role
	#orang yang mau mendaftarkan (harus admin)
	#me-return array user yg sudah di update

	# KAMUS
	# nama, username, passwrod, alamat : string
	# taken, usertakada : boolean = False
	# yorn : string = ""
	
	# ALGORITMA
	if (role == "admin"):
		while True:
			nama = input("masukkan nama : ")
			username = input("masukkan username : ")
			password = input("masukkan password : ")
			alamat = input("masukkan alamat : ")
			#cek username sudah diambil atau belum
			taken = False
			usertakada = False
			yorn = ""
			for b in range(len(arr) -1):
				if (arr[b+1][1] == username):
					taken = True
					break
			if taken:
				print("username sudah diambil, mau memasukkan data ulang?(y/n)")
				while True:
					yorn = input()
					if (yorn == "n" or yorn =="y"):
						break
					else:
						print("input salah,masukkan y/n. (y/n)")
				if (yorn =="n"):
					break
			else:
				break
		#endofwhile
		#data user baru sudah terambil, sekarang masukkan ke dalam file
		if (yorn == "n"):
			# artinya tidak ada data baru yg ditambahkan
			return arr 
		else:
			#resize dulu
			arrbaru = [["" for k in range (len(arr[0]))] for b in range(len(arr)+1)]
			#masukkan data lagi
			for b in range(len(arrbaru)-1):
				for k in range (len (arrbaru[0])):
					arrbaru[b][k] = arr[b][k]
			arrbaru[len(arrbaru)-1] = [str(len(arrbaru)-1),username,nama.title(),alamat,FB01_hashing.hash(password),"user"]
			return arrbaru
	else:
		print("kamu bukan admin, hanya admin yg boleh me-register")
		return arr
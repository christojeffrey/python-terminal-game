# PROGRAM login
# KAMUS
# ALGORITMA
import FB01_hashing
def login (arr):
	# menerima array user,
	# memberikan return nama user dan rolenya jika password benar
	# kalo salah, return string kosong

	# KAMUS LOKAL
	# berhasil : boolean = False
	# role : string =""
	# username : string
	# password : string

	# ALGORITMA
	import sys
	berhasil = False
	role = ""
	username = input("masukkan username : ")
	password = input("masukkan password : ")
	for b in range (len(arr)-1):
		if(arr[b+1][1] == username):
			if (arr[b+1][4] == FB01_hashing.hash(password)):
				role = arr[b+1][5]
				berhasil = True
				break
	if berhasil:
		print("halo", username, ", kamu berhasil login! Rolemu", role)
		return username, role
	else:
		print("gagal, ntah user salah atau password salah")
		sys.exit()
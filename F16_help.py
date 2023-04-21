def help(role):
	print("============HELP============")
	if role == "admin":
		print("register - untuk mendaftarkan pengguna baru")
		print("tambahitem - untuk menambahkan item gadget atau consumable baru(bukan mengubah jumlah item yg sudah ada, harus item baru)")
		print("hapusitem - untuk menghapus item gadget atau consumable")
		print("ubahjumlah - untuk mengubah jumlah item gadget atau consumable yang sudah ada")
		print("riwayatpinjam - untuk menampilkan riwayat peminjaman gadget")
		print("riwayatkembali - untuk menampilkan riwayat pengembalian gadget")
		print("riwayatambil - untuk menampilan riwayat pengambilan consumable")
	if role == "user":
		print("pinjam - untuk meminjam gadget")
		print("kembalikan - untuk mengembalikan gadget")
		print("minta - untuk meminta consumable")
	print("carirarity - untuk mencari gadget berdasarkan rarity")
	print("caritahun - untuk mencari gadget berdasarkan tahun")
	print("save - untuk menyimpan data dalam bentuk csv")
	print("exit - untuk keluar dari program")
# PROGRAM UTAMA
#semua fungsi dipanggil lewat program ini

# KAMUS
# args : array of string (argumen yang diberikan dari argparse)
# lokasi : string (lokasi folder yg akan di load)
# arr_user : array of array of string
# arr_gadget : array of array of string
# arr_consumable : array of array of string
# arr_consumable_history : array of array of string
# arr_gadget_borrow_history : array of array of string
# arr_gadget_return_history : array of array of string
# username : string
# role : string
# inputuser : string (command yang dipilih oleh user)

# ALGORITMA
import argparse
import F01_login
import F02_register
import F03_carirarity
import F04_caritahun
import F05_tambahitem
import F06_hapusitem
import F07_ubahjumlah
import F08_pinjam
import F09_kembalikan
import F10_minta
import F11_riwayatpinjam
import F12_riwayatkembali
import F13_riwayatambil
import F14_load_data
import F15_save_data
import F16_help
import F17_exit
parser = argparse.ArgumentParser()
parser.add_argument("namafolder", help ="nama folder yang akan di load menjadi array")
args = parser.parse_args()
#print("nama foldernya = ",args.namafolder)
lokasi = F15_save_data.carifolder(args.namafolder)
if lokasi == "":
	print("FOLDER TIDAK ADA, TIDAK ADA FILE YG DI LOAD")
else: # load file, siap menerima perintah
	print("============================================================")
	print("selamat datang di kantong ajaib!")
	arr_user, arr_gadget, arr_consumable, arr_consumable_history, arr_gadget_borrow_history, arr_gadget_return_history = F14_load_data.load(args.namafolder)
	print("loading data..\n\n")
	print("silakan login terlebih dahulu")
	username = ""
	role =""
	username,role = F01_login.login(arr_user)
	#sekarang, mencari input hingga exit
	print("siap menerima input! untuk bantuan ketik 'help'")
	while True:
		inputuser = input("->")
		if(inputuser == "login"):
			username,role = F01_login.login(arr_user)
		elif(inputuser == "register"):
			arr_user = F02_register.register(arr_user,role)
		elif(inputuser == "carirarity"):
			F03_carirarity.carirarity(arr_gadget)
		elif(inputuser == "caritahun"):
			F04_caritahun.caritahun(arr_gadget)
		elif(inputuser == "tambahitem"):
			if (role =="admin"):
				arr_gadget, arr_consumable = F05_tambahitem.tambahitem(arr_gadget,arr_consumable)
			else:
				print("hanya untuk admin!")
		elif(inputuser == "hapusitem"):
			if (role =="admin"):
				arr_gadget, arr_consumable = F06_hapusitem.hapusitem(arr_gadget,arr_consumable)
			else:
				print("hanya untuk admin!")
		elif(inputuser == "ubahjumlah"):
			arr_consumable, arr_gadget = F07_ubahjumlah.ubahjumlah(role, arr_consumable, arr_gadget)
		elif(inputuser == "pinjam"):
			arr_gadget, arr_gadget_borrow_history = F08_pinjam.pinjam(role,username,arr_gadget,arr_gadget_borrow_history)
		elif(inputuser == "kembalikan"):
			arr_gadget_borrow_history, arr_gadget_return_history,arr_gadget = F09_kembalikan.kembalikan(role,username, arr_gadget_borrow_history,arr_gadget_return_history,arr_gadget)
		elif(inputuser == "minta"):
			arr_consumable, arr_consumable_history = F10_minta.minta(role,username,arr_consumable,arr_consumable_history)
		elif(inputuser == "riwayatpinjam"):
			F11_riwayatpinjam.riwayatpinjam(role, arr_gadget_borrow_history,arr_gadget)
		elif(inputuser =="riwayatkembali"):
			F12_riwayatkembali.riwayatkembali(role,arr_gadget_return_history,arr_gadget_borrow_history,arr_gadget)
		elif(inputuser == "riwayatambil"):
			F13_riwayatambil.riwayatambil(role, arr_consumable_history,arr_consumable)
		elif(inputuser == "save"):
			print("saving..")
			F15_save_data.save(arr_user, arr_gadget, arr_consumable, arr_consumable_history, arr_gadget_borrow_history,arr_gadget_return_history)
		elif(inputuser == "help"):
			F16_help.help(role)
		elif(inputuser == "exit"):
			F17_exit.exit(arr_user, arr_gadget, arr_consumable, arr_consumable_history, arr_gadget_borrow_history,arr_gadget_return_history)
		else:
			print("input salah, jika bingung ketik 'help'")
		print("===== siap terima input! =====")
#endofwhile
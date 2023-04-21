import sys
import F15_save_data
def exit(arr_user, arr_gadget, arr_consumable, arr_consumable_history, arr_gadget_borrow_history,arr_gadget_return_history):
#merupakan sebuah prosedur untuk keluar program, dengan terlebih dahulu memastikan apakah file ingin di save
	while True:
		yorn = input("apakah mau men-save data dahulu?(y/n)")
		if yorn == "y":
			F15_save_data.save(arr_user, arr_gadget, arr_consumable, arr_consumable_history, arr_gadget_borrow_history,arr_gadget_return_history)
			break
		elif yorn == "n":
			break
		print("input salah, masukkan (y/n)")
	("selamat tinggal!")
	sys.exit()
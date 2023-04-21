#file python untuk fungsi sortbydate descending
def sortbydate(arr,ikt): #ikt = indeks dari kolom tanggal. ARR TANPA JUDUL, LANGSUNG TGLNYA
	#menerima data array dan mereturn data array yg sudah sorted descending(dari yg terbaru)
	#diasumsikan data sudah sesuai format DD/MM/YYYY
	arr = sortby(arr,ikt,6,11) # sort by year
	# print("sorted year,",arr)
	# print("=====================================================================")
	tahunsekarang = arr[0][ikt][6:11]
	start = 0
	for b in range(0,len(arr)):
		# print("ini b",b)
		# print("ini lenarr", len(arr))
		if arr[b][ikt][6:11] != tahunsekarang:
			tahunsekarang = arr[b][ikt][6:11]
			# print("tahun ganti")
			# print("start", start)
			# print("b", b)
			arr = arr[0:start] + sortby(arr[start:b],ikt,3,5) + arr[b:len(arr)] # sort by month for every year
			start = b
		if b == len(arr)-1 and tahunsekarang == arr[b][ikt][6:11]:
			# print("start", start)
			# print("b", b)
			# print("cek dlu")
			# print(arr[start:b+1])
			arr = arr[0:start] + sortby(arr[start:b+1],ikt,3,5) + arr[b+1:len(arr)]
	# print("sorted month,",arr)
	# print("tes")
	# print(arr)
	bulandantahun = arr[0][ikt][3:11]
	start = 0
	# print("=====================================================================")
	# print("Day lenarr", len(arr))
	for p in range(0,len(arr)):
		# print("ini P", p)
		# print("arr p",arr[p][ikt][3:11] )
		if arr[p][ikt][3:11] != bulandantahun:
			# print("tadi bulan", bulandantahun)
			bulandantahun = arr[p][ikt][3:11]
			# print("ganti bulan, sekarang jadi",bulandantahun)
			# print("start = ", start, "p  = ", p)
			arr = arr[0:start] + sortby(arr[start:p],ikt,0,2) + arr[p:len(arr)]# sort by date every month
			start = p
		if p == len(arr)-1 and bulandantahun == arr[p][ikt][3:11]:
			arr = arr[0:start] + sortby(arr[start:p+1],ikt,0,2) + arr[p+1:len(arr)]
		# print("ini p", p,"ini arr\n", arr)
	return arr

def sortby(arr,ikt,iis,fis): # iis = initial index of substring, fis = final index of substring 
	# print("arr di sortby", arr)
	for b in range(0, len(arr)):
		maks = int(arr[b][ikt][iis:fis])
		for k in range(b, len(arr)):
			# print("compare", int(arr[k][ikt][iis:fis]), maks)
			if int(arr[k][ikt][iis:fis]) > maks:
				maks = int(arr[k][ikt][iis:fis])
		# print("maks ", maks)
		idxmaks = b
		for k in range(b,len(arr)):
			# print(int(arr[k][ikt][iis:fis]), maks)
			if int(arr[k][ikt][iis:fis]) == maks:
				idxmaks = k
				# print("idx maks = ", idxmaks)
				# print("b = ",b)
				# print("swap", arr[b], arr[idxmaks])
				break
		#skarang di swap
		temp = arr[b]
		arr[b] = arr[idxmaks]
		arr[idxmaks] = temp
	# print("arr abis sortby",arr)
	return arr 

# coba = [["30/10/2020",1],
# 		["31/10/2020",2],
# 		["29/10/2020",3],
# 		["12/11/2020",4],
# 		["04/21/2020",5],
# 		["04/12/2021",6],
# 		["12/12/2012",7],
# 		["17/03/2013",8],
# 		["04/21/2020",9]]
# sorted = sortbydate(coba,0)
# print("PRINT!")
# for line in sorted:
# 	print(line)
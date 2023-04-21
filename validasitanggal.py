def validasitanggal(kata):
	#return true jika format sudah seusai DD/MM/YYYY
	if len(kata) != 10:
		return False
	if not(kata[0:2].isdigit()) or not(kata[3:5].isdigit()) or not(kata[6:10].isdigit()):
		return False
	if kata[2:3] != "/" or kata[5:6] != "/":
		return False
	d = int(kata[0:2])
	m = int(kata[3:5])
	y = int(kata[6:10])
	if y < 0:
		return False
	else:
		if m < 0 or m > 12:
			return False
		else:
			if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
				if d < 0 or d > 31:
					return False
			elif m == 2:
				if y % 400 == 0:
					if d< 0 or d > 29:
						return False
				elif y % 100 == 0:
					if d < 0 or d > 28:
						return False
				elif y % 4 == 0:
					if d < 0 or d > 29:
						return False
				else:
					if d < 0 or d > 28:
						return False
			else:
				if d < 0 or d > 30:
					return False
	return True

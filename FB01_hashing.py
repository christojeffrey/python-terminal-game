def hash(password):
	p = 256
	m = 1000000009
	hasil = 0
	p_pangkat = 1

	for c in password:
		hasil = (hasil + (ord(c)) * p_pangkat) % m
		p_pangkat = (p * p_pangkat) % m
	return str(hasil)

#Please install PyPDF2 to run this program!
#!pip install PyPDF2
import itertools
import PyPDF2

#products = [9135, 6565, 10682, 3266, 7638, 6912, 7488, 1368]
#I used factordb to factorize every number
#I made sure that every multiple is in the range of 33-125
"""
9135 = 3^2 x 5 x 7 x 29 = 87 x 105
6565 = 5 x 13 x 101 = 65 x 101
10682 = 2 x 7^2 x 109 = 98 x 109
3266 = 2 x 23 x 71 = 46 x 71
7638 = 2 x 3 x 19 x 67 = 67 x 114
6912 = 2^8 x 3^3 = 64 x 108
7488 = 2^6 x 3^2 x 13 = 64 x 117
1368 = 2^3 x 3^2 x 19 = 98 x 116

"""

sets = [(87, 105),(65, 101),(98, 109),(46, 71),(67, 114),(64, 108),(64, 117),(98, 116)]
possible_arrays = list(itertools.product(*sets))

#print("Possible passwords: ")
with open('Final soln_protected.pdf', 'rb') as pdf:
	pdf_file = PyPDF2.PdfReader(pdf)
	for p in possible_arrays:
		password=""
		for i in p:
			password+=chr(i)
		print(password)
		try:
			if pdf_file.decrypt(password) == 2:
				print(f"\nPassword Found!!!: {password}")
				break
		except:
				pass

"""
Alternatively, in stage-2 they gave a hint "Web.Club" so assuming this as one of the 
string we can find the other string which we will directly get as "iAmGr@@t"

"""
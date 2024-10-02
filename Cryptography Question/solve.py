enc_string="YZH(878GBC 8BFC87 8C7999 F8AFB ADA8GG 8GGCC7 A7F9EG 8BFDAB)"

alphabets_nums=[str(i) for i in range(0,10)]
alphabets_chars=[chr(i) for i in range(ord('A'),ord('Z')+1)]
alphabets=alphabets_nums+alphabets_chars  # Including both alphs and nums

ceaser_shift=""
shift=7 # Using a ceaser shift of 7
for c in enc_string:
	for i in range(len(alphabets)):
		if(c==alphabets[i]):
			ceaser_shift+=alphabets[i-shift]
	if(c not in alphabets):
		ceaser_shift+=c

print(ceaser_shift)




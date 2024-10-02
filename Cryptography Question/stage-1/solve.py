n = 421649
e = 17
"""
I used factordb to factorize 'n'
"""
p = 557
q = 757
#cip=10194514851015022281384363199199550308279148634
cips=[101945, 148510, 150222, 81384, 363199, 199550, 308279, 148634]

phi = (p-1)*(q-1)
d=pow(e,-1,phi)

decrypted=""
for cip in cips:
	pt=pow(cip,d,n)
	decrypted+=str(pt)
	decrypted+=" "
print(decrypted)
# 9135 5700 6382 9648 7286 4198 1686 3054
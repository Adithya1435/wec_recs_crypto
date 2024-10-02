encrypted_values=[9135,5700,6382,9648,7286,4198,1686,3054]

#Accepted ascii values = 33 to 125
min_value=33*33
max_value=125*125

products=[]

for i in range (len(encrypted_values)):
	if(i==0):
		products.append(9135)
	else:
		l=(10000*(0) + encrypted_values[i]) - encrypted_values[i-1]
		r=(10000*(1) + encrypted_values[i]) - encrypted_values[i-1]
		#as all values in encrypted_values are less than 10000 we can check only for 0 and 1
		if(l>min_value and l<max_value):
			products.append(l)
		elif(r>min_value and r<max_value):
			products.append(r)

print(products)

#Output - [9135, 6565, 10682, 3266, 7638, 6912, 7488, 1368]

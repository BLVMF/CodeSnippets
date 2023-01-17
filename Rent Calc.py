import math
rent = 2070.60
i = 0 
rentplus = rent +(rent * 0.02)
totalover10 =[]
year = 2023


for i in range(10):
	rentplus = rentplus + ( rentplus * 0.015)
	print(year,rentplus)
	yearlytotal = rentplus * 12
	totalover10.append(yearlytotal)
	i += 1
	year += 1
	


how_much_spent = sum(totalover10)
print(math.floor(how_much_spent))

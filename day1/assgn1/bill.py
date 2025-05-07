units = int(input("Enter bill units"))
bill = 0


if units-200>0:
	bill += (units-200)*10+(100*5)
elif units-100>0:
	bill += (units-100)*5
else:
	bill = 0
print("Total bill : ",bill)


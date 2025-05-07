n = int(input("Enter number of classes held"))
att = int(input("Enter number of classes attended"))

percent = (att/n)*100
if percent >= 75:
	print("Attendance : ", percent, " allowed")	
else :
	print(percent)	
	inp = input("Do you have medical cause ('Y' or 'N')")
	if inp == "Y":
		print('Allowed')
	else :
		print('Not Allowed')


year = int(input("Enter the year"))

if ((year%100==0)&(year%400==0)) | ((year%4==0)&(year&100!=0)):
	print("LEAP YEAR")
else:
	print("Not a leap year")

amt = int(input("Enter amount"))

if amt//2000>0:
	note_2k = amt//2000
	amt = amt%2000
	print("2000 - ", note_2k," note")
if amt//500>0:
	note_5h = amt//500
	amt = amt%500
	print("500 - ",note_5h," note")
if amt//100>0:
	note_1h = amt//100
	amt = amt%100
	print("100 - ",note_1h," note")
if amt//50>0:
	note_50 = amt//50
	amt = amt%50
	print("50 - ", note_50," note")
if amt//10>0:
	note_10 = amt//10
	amt = amt%10
	print("10 - ",note_10," note")
if amt//5>0:
	note_5= amt//5
	amt = amt%5
	print("5 - ",note_5," coin" )	
if amt//2>0:
	coin2 =amt//2
	amt = amt%2
	print("2 ",coin2," coin")
if amt//1>0:
	coin1 = amt//1
	print("1 ",coin1," coin")

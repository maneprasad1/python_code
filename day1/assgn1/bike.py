price = int(input("Enter cost price of bike"))

if price>100000:
	tax = price*0.15
	ins = price*0.20
	print("Tax ",tax, " Insurance ", ins, " Total ",price+tax+ins)
elif 50000<price<=100000:
	tax = price*0.10
	ins = price*0.08
	print("Tax ",tax, " Insurance ", ins, " Total ",price+tax+ins)
elif price<=50000:
	tax = price*0.05
	ins = price*0.05
	print("Tax ",tax, " Insurance ", ins, " Total ",price+tax+ins)


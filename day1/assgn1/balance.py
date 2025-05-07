#! usr/bin/python3

# acc balance as input if >50k then more 10kto49999 in between <10k less
marks = int(input("Enter account balance "))

if marks >=50000:
	print("MORE")
elif (marks >=10000) and (marks<49999):
	print("In between")
else :
	print("LESS")

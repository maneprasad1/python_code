
inp = input("Enter numbers ")
digits = inp.split(",")

res = map(lambda x : float(x), digits)
print(list(res))

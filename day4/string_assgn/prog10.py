

string = input("Enter a string ")
new = ''

new += string[-1]
new += string[1:-1]
new += string[0]

print(new)

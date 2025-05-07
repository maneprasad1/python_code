

string = input("Enter a string ")

words = string.split(',')
words.sort()

new = ",".join(words)
print(new)


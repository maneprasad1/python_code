

#count total num of words in sent find avg len of all words in sentence

s  = input("Enter sentence  ")

words = s.split(" ")

n= len(words)
print("COunt of words ",n)
length = 0

for i in words:
	length += len(i)

print("Average length ", length/n)

#combine all words without spaces and print reverse of string

new_str = ''.join(words)
print(new_str[::-1])

#from the given sentence all the capital letters should come at end and
# result should not have any spaces

s1=''
s2=''
for i in new_str:
	if i.isupper():
		s1+=i
	else:
		s2+=i

print(s2+s1)

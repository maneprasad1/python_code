
list1 = ['red','green','white','black','pink','yellow']
new_list = [x for i,x in enumerate(list1) if i not in (0,4,5)]
print(new_list)
del list1[5]
del list1[4]
del list1[0]

print(list1)



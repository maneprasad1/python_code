
import copy
l1 = [1,2,3,4,5]

l2 = l1.copy()
l3 = l1
l4 = copy.deepcopy(l1)

print("Using copy() ",l2)
print("Using assgn ",l3)
print("Using deepcopy ",l4)

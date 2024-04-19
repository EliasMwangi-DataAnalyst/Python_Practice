# create an empty list called my_list
my_list = []

# append elements to the list
my_list.append(18)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# insert the value 15 at the second position
my_list.insert(1, 15)

print(my_list)

# extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

print(my_list)

# remove the lst element from my list
my_list.pop()

print(my_list)

# sort in ascending order
my_list.sort()

#find and print index of value 30
print(my_list.index(30))

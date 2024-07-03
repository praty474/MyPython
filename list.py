# list tuple set dictionary
# non primitive 

#list is heterogenous, mutable 

list = [1, 2, 4, 3, 8, 5, 6]
#       0  1  2  3  4  5
#      -6 -5 -4 -3 -2 -1

print(list)

# printing specific index 
print(list[2])
print(list[0:2])

# list allows duplicate values

# length of list
print(len(list))

# list can contain different data types

# check item in list
if 3 in list:
    print('yes')

# changing value 
# list[1] = 55
# print(list)

# insert item
list.insert(3,"new")
print(list)

list.copy()
# add item
list.append("notebook")
print(list)

# remove
list.remove(3) #value

# pop
# remove specific index
list.pop(1)
# remove last item
list.pop()

x = list.copy()

print('x is',x) #The copy() method returns a copy of the specified list.



#extend
#copy
#tuple set dictionary
#loop


# A set is a collection which is unordered, unchangeable*, and unindexed
# if you want to store unique value use set

myset = {'Ram', 'Hari', 'Ramesh'}

print(myset)

# do not allow duplicate values.
# Set items can appear in a different order every time you use them, 
# and cannot be referred to by index or key

# Duplicate values will be ignored:

# True and 1 are considered the same value in sets

# get length
print(len(myset))

print(type(myset))

#loop through

for x in myset:
  print(x)

#present
print('Ramesh' in myset)


#adding item

myset.add('Sita')

# add sets 
set2 = {'Kc', 'kayastha', 'shrestha'}
myset.update(set2) #update can be list or tuples

#REMOVE
myset.remove('Ram')

# del to delete set completely
# clear() method empties the set:


#join sets
set3 = {11, 2, 33}
set4 = {1, 2, 3}

set5 = set3.union(set4)
# set5 = set3.union(set4, set2)
# set5 = set3 | set4 
# union or |
print(set5)

#intersection or &
set6 = set3.intersection(set4)
print(set6)

# differnce
set7 = set3.difference(set4)

# method will keep only the elements that are NOT present in both sets
set8 = set3.symmetric_difference(set4)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

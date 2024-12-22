

my_array = [1, 2, 3, 4, 5, 6, 7]
next_array = [10, 12, 23, 34, 45, 56, 67]
new_array = [1, 1, 1, 2, 2, 3, 3]
array_1 = [1, 2, 3, 2, 3, 1, 1, 2, 2, 3, 3]

# print(my_array[1:4])
# print(my_array[:4])
# print(my_array[::2])
# print(my_array[::-1])

my_array.append(8)
my_array.insert(1,9)
my_array += [100]
my_array += next_array

my_array.pop()
my_array.pop(0)
my_array.remove(45)
new_array.remove(3)
array_1.remove(3)

print(len(my_array))
print(len(my_array)-1)
print(my_array[-1])
print(my_array[-1])


print(new_array)
print(my_array)
print(array_1)

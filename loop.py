# while loop

i = 1

while i< 10:
    print(i)
    i += 2

while i < 101:
   if i % 2 == 0:
      print(i)
   i += 1


while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# for loop
# for loop can be applied to string, set, tuple, list, dict and range 

#string
for x in "laptop":
   print(x)

#list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
   print(fruit)

# break

for fruit in fruits:
   print(fruit)
   if x == "banana":
      break
# break current and next iteration

# continue 
# temporary break
# break current iteration
num = [1, 2, 3, 4]
for i in num:
   if i % 2 == 0:
      continue
      print('Hello')
   else:
      print(i)

   
# range

for x in range(2, 10, 2):
   print(x)

for x in range(2, 10, 2):
   print(x)
else:
   print('over')


i = 5
for j in range(1,11):
    print(f'{i} * {j} =', i * j)
    j += 1


#nested loop


for i in range(5):
    for j in range(i + 1):
      print('*', end = '')
    print()

# tab  
# shift tab 
# Tuples are used to store multiple items in a single variable.
# ordered and unchangeable
# heterogenous
# use tuple for never changing values ie. days in week etc
tuple1 = ('Ram', 'Hari', 'Ramesh' )
tuple2 = (1, 2, 3)


print(tuple1)
print(len(tuple1)) #length of tuple

print(type(tuple1))


#access tuple
print(tuple1[1]) 
print(tuple1[:2]) 

print('Ram' in tuple1) #check if item exist


(Kc, kayastha, shrestha) = tuple1
# we are also allowed to extract the values back into variables. This is called "unpacking"
print(Kc)

#loop through tuple

for x in tuple1:
    print(x)

#joining tuple

tuple3 = tuple1 + tuple2
print(tuple3)

#multiply tuple
mul = tuple1 * 2
print(mul)


names = ('Ram', 'Hari', 'Shyam')

a = list(names)

a.append('Rita')

names = tuple(a)

print(names)




b = ['ram', 'shyam', 'ram', 'rita', 'rita']

print(len(set(b)))

# tuple=()
# dict={}
# set = {}
list = []
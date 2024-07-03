# Dictionaries are used to store data values in key:value pairs.
# changeable and do not allow duplicates.
# a = {} is dictionary not set

dict1 = {
    "name": "Ram",
    "age": 12,
    "class": 8,
    "hobbies": ["dancing", "singing"]
}

print(dict1)

print(dict1["age"])

# Duplicate values will overwrite existing values: key should be unique

print(len(dict1))

print(type(dict1))


x = dict1.get('class')
y = dict1.keys()
z = dict1.values()

print(x)
print(y)

# add new item
dict1["ln"] = "kc"
# if key exist value will be updated

print(y)


# check if key exist
print("age" in dict1)

# change dict items 
dict1["age"] = 22
dict1.update({"age" : 25})

dict1.pop("class")
dict1.popitem()

# del dict["ln"]


for x, y in dict1.items():
    print(x,y)
for x in dict1.values():
    print(x)

dict2 = dict1.copy()
# or
dict2 = dict(dict1)


# gives list of tuples
print(dict1.items())


#Nested Dictionary

info = {
    'name' : 'Umesh',
    'address':{'city': 'balaju', 
               'district': 'ktm'}
}

print(info['address']['city'])


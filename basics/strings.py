

text = 'Hello World'

text2 = 'John\'s car'

text3 = "John's car"

text4 = """John's
car"""

print(text2)
print(text2)
print(text4)


# length of string
print(len(text))
print(text[0])


# slicing 
print('slicing',text[0:7:1])
print(text[:4]) # 0 to 3
print(text[::-1]) #reverse
# first index is inclusive but second index is not
#[start:end:step]


#lowercase
print(text.lower())

#count
print(text.count('l'))

# find
print(text.find('World'))
print(text.find('World war')) #gives -1 if not present

# Replace
replaced = text.replace('World', 'Universe')
print(replaced)

#string concat
greeting = 'Hello'
name = 'pratyush'

message = greeting + ", " + name
message2 = '{}, {}. Welcome!'.format(greeting, name)
message3 = f'{greeting}, {name.capitalize()}. Welcome!'
print(message)
print(message2)
print(message3)

# all available methods
# print(dir(name))


# upper()
# lower()
# capitalize()
# title()
# replace()
# string()
# endswith()
# startswith()
# index()
# count()
# format string



text = 'Hello, world'
text2 = ' hello '
text3 = 'hello world'

print(text.upper()) #returns the string in upper case:

print(text.lower()) #returns the string in lower case:

print(text2.strip()) #removes any whitespace from the beginning or the end

print(text2.lstrip()) #removes any whitespace from the beginning or the end

print(text2.rstrip()) #removes any whitespace from the beginning or the end

print(text.replace('o', 'i')) #replace a string 

print(text.split(',')) #method returns a list where the text between the specified separator becomes the list items

print(text3.capitalize()) #capitalize first character

print(text3.title()) #each word is title cased

print(text3.endswith('d')) #returns bool if strings end with particular character

print(text3.startswith('d')) #returns bool if strings starts with particular character

print(text3.index('d')) #returns index of particular char

print(text3.index('l', 3)) #returns index of particular char

print(text3.count('l')) #count total no. of character in string



# string formatting
name = 'Pratyush'
price = 19.1252

sentence = "My name is " + name
sentence2 = f"My name is {name}"
sentence3 = f"The price is {price:.2f}" #2f 2 decimal point
sentence4 = f"The price is {price*2:.2f}" #we can perform math operation

print(sentence)
print(sentence2)
print(sentence3)
print(sentence4)


# strings, int, float, bool are immutable


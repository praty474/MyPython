
# 2 write a function that takes string as an argument and return reversed of string

def reversed_string(word):
    print(f'reversed word is {word[::-1]}')

userInput2 =input("Enter a word ")

reversed_string(userInput2)

# 3 write a function that takes string as an argument and return length of string

def string_length(word):
    print(f'length of word {word} is {len(word)}')

string_length(userInput2)

# 4 write a function that takes string as an argument and return first char of string

def first_character(word):
    print(f'First character of {word} is {word[0]}')

first_character(userInput2)

# 5 write a function that takes string and returns true if first char is upper case else return false

def first_char_uppercase(word):
    if (word[0]).isupper():
        print(f'First char of {word} is uppercase')
    else:
        print(f'First char of {word} is uppercase')

first_char_uppercase(userInput2)

# 6 write a function that takes string as an argument and return last char of string

def last_char(word):
    print(f'Last character of {word} is {word[-1]}')

last_char(userInput2)

# 7 write a function that takes string as an argument and check if digit is present in the string

def if_digit_present(word):
    digit = '1234567890'
    count = 0
    for char in range(len(word)) :
        if word[char] in digit:
            count += 1
    if count >= 1:
         print(f'Digit present')
    else:
        print('No digits')

if_digit_present(userInput2)

def if_digit_present(word):
    digit = '1234567890'
    for char in word:
        if char == digit:
            print('yes')
            
if_digit_present(userInput2)

# 8 write a function that takes string as an argument and check if palindrome or not disregarding case sensitivity 

def palindrome(word):
    lower_word = word.lower()
    reversed = lower_word[::-1]

    if lower_word == reversed:
        print('palindrome')
    else:
        print('not')

palindrome(userInput2)

# 9 write a function that takes string as argument the count of the letter U present in the string without using count disregarding case sens

def count_letter_u(word):
    lowered = word.lower()
    count = 0
    letter = 'u'
    for char in lowered:
        if char == letter:
            count +=1
    print(count)

count_letter_u(userInput2)

# 10 write a function that takes string as argument whether letter u is present or not

def if_u_present(word):
    lowered = word.lower()
    letter = 'u'

    for char in lowered:
        if char == letter:
            return True
        
if_u_present(userInput2)

if if_u_present(userInput2) == True:
    print('True')
else:
    print('False')

# 11 write a function that takes list of numbers as argument  and return list of number with only even number

list = [1, 2, 3, 4, 5, 8, 9, 16]

def even_only_list(list):
    list2 = []
    for i in list:
        if i % 2 == 0:
            list2.append(i)
    print(list2)
even_only_list(list)

# 12 write a function that takes multiple number and return maximum of those number

def max_num(list):
    max_num = 0

    for i in list:
        if i > max_num:
            max_num = i
    print(max_num)

max_num(list)


#13 write a function that takes a string as a argument and check whether vowels are present
def if_vowel_present(word):
    lowered = word.lower()
    vowels = 'aeiou'
    string = ''
    count = 0
    for char in range(len(lowered)) :
        if lowered[char] in vowels:
            count += 1
            string += lowered[char]
    if count >= 1:
        print(f'{count} vowels present {string}')
    else:
        print('No vowels')
            
if_vowel_present(userInput2)

# 14 write a function that takes a string as a argument and check whether consonant is present or not

def if_consonant_present(word):
    lowered = word.lower()
    vowels = 'aeiou'
    string = ''
    count = 0
    for char in range(len(lowered)) :
        if lowered[char] not in vowels:
            count += 1
            string += lowered[char]
    if count >= 1:
        print(f'{count} consonant present {string}')
    else:
        print('No consonant')
        
if_consonant_present(userInput2)

# 15 write a function that takes a string as a argument and returns the first vowel present in string

def first_vowel (word):
    lowered = word.lower()
    vowels = 'aeiou'
    string = []
    count = 0
    for char in range(len(lowered)) :
        if lowered[char] in vowels:
            count += 1
            string += lowered[char]
    if count >= 1:
        print(f'First vowel is {string[0]}')
    else:
        print('No vowels')

first_vowel(userInput2)

# 16 write a function that takes a string as a argument and returns the first consonant present in string

def first_consonant(word):
    lowered = word.lower()
    vowels = 'aeiou'
    string = []
    count = 0
    for char in range(len(lowered)) :
        if lowered[char] not in vowels:
            count += 1
            string += lowered[char]
    if count >= 1:
        print(f'First consonant is {string[0]}')
    else:
        print('No consonant')

first_consonant(userInput2)

# 17 write a function that takes a string as a argument and returns the total number of vowels present in string

def count_vowel (word):
    lowered = word.lower()
    vowels = 'aeiou'
    count = 0
    for char in range(len(lowered)) :
        if lowered[char] in vowels:
            count += 1
    if count >= 1:
         print(f'Total no. of vowels are {count}')
    else:
        print('No vowels')

count_vowel(userInput2)

# 18 write a function that takes a string as a argument and returns the total number of consonant present in string


def count_consonant (word):
    lowered = word.lower()
    vowels = 'aeiou'
    count = 0
    for char in range(len(lowered)) :
        if lowered[char] not in vowels:
            count += 1
    if count >= 1:
         print(f'Total no. of consonant are {count}')
    else:
        print('No consonant')

count_consonant(userInput2)
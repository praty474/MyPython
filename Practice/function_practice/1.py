# 1 write a function that takes number as an argument and return true  if even or false

def odd_even(number):
    if userInput % 2 == 0:
        print(f'{number} is even')
        
    else:
        print(f'{number} is odd')    

userInput = int(input('enter a number '))

odd_even(userInput)

# 19 write a function that takes a number and returns list of even number upto that number without using range

def list_of_even_numbers(number):
    even_num = []
    i = 0
    
    while i <= number:
        if i % 2 == 0:
          even_num.append(i)
        i += 1
    
    return even_num

print(list_of_even_numbers(userInput))

list_of_even_numbers(userInput)

# 20 write a function that takes a number as argument and returns list of even and odd  number upto that number without using range

def list_of_even_odd_numbers(number):
    even_num = []
    odd_num = []
    i = 0
    
    while i <= number:
        if i % 2 == 0:
            even_num.append(i)
           
        else:
            odd_num.append(i)
        
        i += 1
    
    return odd_num, even_num

print(list_of_even_odd_numbers(userInput))


list_of_even_odd_numbers(userInput)
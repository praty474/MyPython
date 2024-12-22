
a = 11
if a < 5:
    print(a)
else:
    print('error')
# indentation should be followed

# if multiple condition is there use elif


if a < 5:
    print(a)
    #elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
elif a < 6:
    print('error')
elif a < 7:
    print('error')
else:
    print('ok')

# and ko case ma sajilo condition agadi lekhney


if a < 1:
    pass


# input 
# if and else



# short hand if 
# if only one statement then it can be written in same line 
if a > 5: print('ok')


# multiple else statements on the same line using ternary operators
num1 = 300
num2 = 500
num3 = 600
print('num1') if num1 > num2 else print('=') if num1 == num2 else print('num2')


# and 
if num2 > num1 and num2 > num3:
    print('and true')
# or
if num2 > num1 or num2 > num3:
    print('or true')
# not
if not num2 > num3:
    print('yes')


#nested

if num3 > num2:
    print('greater than num2')
    if num3 > num1:
        print('greater than num1')
    else:
        print('not greater')
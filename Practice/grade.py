
student = {
    'ram' : 80,
    'shyam' : 45,
    'ramesh' : 75,
    'hari' : 25,
}

name = input('Enter your name ').lower()

if name in student:
    print(f'{name.capitalize()} your marks is {student[name]}')
    if student[name] >= 80 :
        print('You secured distinction')
    elif student[name] >= 60:
        print('You secured first division')
    elif student[name] >= 40:
        print('You secured second division')
    else:
        print(f"Mom's flying chapal received at {student[name]}km/hr")

else: 
    print(f'{name.capitalize()} not found')

# if greater than 80 distinction
# print(f"Mom's flying chapal received at {student[name]}km/hr")

# loop and function
# package and module
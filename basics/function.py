# creating function 

def function():
    print("This is function")

# calling function

function()

# Information can be passed into functions as arguments or parameters
# multiple arguments separated using ,

def name_function(fname):
    print("Hello " + fname)

name_function("Hari")
name_function("Harish")

# multiple args
def full_name_function(fname, lname):
    print(f"Hello {fname} {lname}")

full_name_function("Hari", "Ram")
# full_name_function("Hari") #this will give error
full_name_function("Harish", "Ram")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into 
# your function, add a * before the parameter name
# function will receive a tuple of arguments

def new_function(*students):
    print("this is arbitrary args " + students[0])

new_function("ram", "hari")

# Keyword Arguments
# key = value syntax
# order of the arguments does not matter

def my_function(student3, student2, student1):
  print("The youngest child is " + student3)

my_function(student1 = "Emil", student2 = "Tobias", student3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** 
# before the parameter name in the function definition
# receive a dictionary of arguments,

def my_function(**child):
    print(child["name"])

my_function(name = "Ram", lname = "Hari")

# Default Parameter Value

def default(city = "KTM"):
    print("I am from " + city)

default()
default("BKT")

# passing list as an argument
 
def list_argument(subject):
    for x in subject:
        print(x)
    
subject_name = ["Science", "Math"]

list_argument(subject_name)

# return
# if you want to use the value function outside function use return
# if we dont return anything if returns null
# can return multiple value it is stored in tuple
def return_statement(x):
    return 2 * x
print(return_statement(6))

# The pass Statement
# function definitions cannot be empty, 
# put in the pass statement to avoid getting an error.

def empty():
    pass

# Positional-Only Arguments

def positional_args(y, x, /):
    print(x / y)

positional_args (2, 6)

# keyword-only args
def keyword_only(x):
    print(x)

keyword_only(5)

# Recursion
# function can call itself

def recursion(x):
    if (x > 0):
        res = x + recursion(x - 1)
        print(res)
    else:
        res = 0
    return res

recursion(4)


# python package is way to organize and structure your 
# python code into reuseable component

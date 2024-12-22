# def define

def add(i, j): 
    print(i +j)

add(2, 3)
# here i = 2 and j = 3

# types of arguments

# positional arguments - where order matters 
# if order gets mismatched output can be wrong

# keyword argument
add(j = 3 , i = 6)



# you cant have function with the same name 


# multiple / variable length positional argument

# stored in tuple

def sub(*args):
    print(args)

#  multiple length keyword argument
# stored as dictionary

def mul(**kwargs):
    print(kwargs)
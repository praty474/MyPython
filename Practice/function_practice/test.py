print('hello world')

# syntax error
# logical error
# runtime error (exception)

while True:
    try:
        a = int(input('Enter a first num '))
        b = int(input('Enter a second num '))
        print(a/b)
    except ValueError:
        print('Input must be numbers')
    except ZeroDivisionError:
        print("Second num can't be zero")
    except:
        print('error')
    finally:
        print('Thank you')

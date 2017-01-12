# Arguments to a function
# Positional Arguments
'''
def add(x, y):
    return x + y

print(add(13, 18))
'''

# Keyword Arguments
'''
def yell(phrase = 'Stoop!!'):
    print(phrase)

yell()
yell(phrase = 'Right there!!')
'''

# Postional and keyword arguments
'''
def echo(text, prefix=''):
    print('{0}{1}'.format(prefix, text))

echo('buttonbox')
echo('hello', prefix='> ')
'''

# Arbitrary
'''
def some_method(*args, **kwargs):
    print(args)
    print(kwargs)

some_method(1, 2, 3, name='numbers')
'''


# First n numbers of Fibonacci Sequence
'''
def fib(n):
    result = []
    a, b = 0, 1
    for x in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fib(10))
'''


# Error handling
try:
    num = int(input('Enter a number'))
    print(num)
# Basic catch expression
except ValueError:
    print('Oops!')

try:
    num = int(input('Enter a number'))
# multiple catch
except (ValueError, TypeError):
    print('Thats not a number')

try:
    num = int(input('Enter a number'))
# different exceptions
except ValueError:
    print('Thats not a number')
except TypeError:
    print('Cant convert to a number')


def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by Zero')
    else:
        print('result is ', result)
    finally:
        print('executing finally clause')

div(3, 0)

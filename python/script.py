# print("Welcome to Python!")

"""
import datetime
print(datetime.datetime.now())

from datetime import datetime
print(datetime.today().date())

from datetime import datetime as dt
print(dt.today().date())
"""


# string variable (single or double quotes. both work)
# name = "Pratima"
# print(name + " Sakinala")

# multi-line string (3 single or double quotes)
# address = '''5510 N Milburn Ave,
# Apt 204,
# Fresno, CA'''
# print(address)


# number variable
# year = 2016
# year = int('2016')
# print(year)


# float number
# pi = 3.14159
# pi = float('3.14159')
# print(pi)


# fixed-point number
# from decimal import Decimal
# price = Decimal('9.99')
# print(price)


# boolean
is_python = bool('any object')
# print(is_python)
falsey_values = False or 0 or '' or [] or {} or None
# print(bool(falsey_values))
true_values = True and 1 and 'text' and ['q', 'w'] and {'e':'r'}
# print(bool(true_values))


# List (equivalent to array in JS)
# fruits = ['banana', 'apple', 'orange', 'kiwi']
# print(fruits)
# print(len(fruits)) # length of fruits list
# print(fruits[1:]) # prints all items in fruits list after index 1 (including 1)
# print(fruits[-1]) # prints last item in fruits list
# fruits.append('pineapple') # adds pineapple to fruits list (same as push in JS)
# fruits.extend(['mango', 'strawberry']) # extends fruits list with another list
# fruits.insert(1, 'cherry')
# print(fruits)


# dictionary (equivalent to object in JS)
person = {'name': 'Pratima Sakinala'}
# print(person['name']) # to capture the value of a key or next line can also be used
# print(person.get('name'))
person['birthday'] = 'July 13' # set a value to key
person.update({
    'hobbies': ['crafting', 'travelling'],
    'gender': 'female'
})
# print(person)
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.get('favorite_color', 'blue')) # doesn't add to person dictionary
# print(person)
# del person['birthday'] # removes key and its value


# ask user input:
# num = raw_input('Enter a number')
# print(num)

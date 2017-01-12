# if, elif and else
'''
grade = 91
if grade > 90:
    if grade == 100:
        print('A+')
    else:
        print('A')
elif grade > 80:
    print('B')
elif grade > 70:
    print('C')
else:
    print('F')
'''

# for loop
'''
for x in range(100):
    if ((x % 3 is 0) and (x % 5 is 0)):
        print('Fizz Buzz')
    elif x % 3 is 0:
        print('Fizz')
    elif x % 5 is 0:
        print('Buzz')

fruits = ['banana', 'orange', 'apple']
for fruit in fruits:
    print(fruit)
'''

# Extended for loop
states = {
    'CA' : 'California',
    'OR' : 'Oregon',
    'AZ' : 'Arizona'
}
for key, value in states.items():
    print ('{0} : {1}'.format(key, value))

# while loop
'''
x = 0
while x < 100:
    print(x)
    x += 1
'''

# List comprehensions
odds = [x for x in range(100) if x % 2]
# print(odds)

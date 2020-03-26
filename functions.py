'''
examples of built in function

len()
input()
lower()
upper()
islower()

- How to write function
def function_name():
    code
- how to call function
 function_name()

- type of functions

a- does not return value ( display text)
b- return value ( calculate tmeperatre or curreny)
'''

# simple function with no parameters


def hello():
    print('hello')
    print('welcome to my program')


hello()
# function with parameters


def hello2(name):
    print(f'hello {name}')
    print('how are you today')


hello2('ali')

# a - sum two number

a = 10
b = 20


def total(num1, num2):
    return num1 + num2


print(total(a, b))
print(total(20, 40))

# convert temp from f to c
# c = (F − 32) × 5/9


def convert_f_to_c(f):
    c = (f - 32) * 5/9
    return round(c, 4)


print(convert_f_to_c(70))

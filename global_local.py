# variables in python can be local or global
# it is important to know the differnce

# local scope example
# if  you want to access variable from all program keep it global
# if you to change inside function- add global variable_name

age = 20


def myage():
    age = 14
    name = "Ahmed"
    print(age)

# global to change variable 
def myage2():
    global age
    age = 30


myage()
myage2()
print(age)

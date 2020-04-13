
'''
TO import module you can use :

1- import module_name
This will make all content private and can only be accessed from module name
 like mod.convertToKG()
'''

# import mod

# print(mod.convertToKG(1300))

# print(mod.animales)

''''
2- from module_name import name(s)
 or from module_name import *
'''

# from mod2 import OMR_To_Dollar
# print(OMR_To_Dollar(100))

'''
3- from module_name import name as newName

'''


import sys
import mod2 as myMod
from mod import convertToG as ToG
print(ToG(10))

'''
import module_name as new_name
'''

# sys
print(sys.path)
print(myMod.__file__)
# print(dir())

print(dir(myMod))


'''

you can pack all related modules in one Packahge
'''

# How to create Lists

list1 = [1, 2, 3, 4, 5]
print(list1)
# access item in the list
print(list1[0])
print(list1[-1])
print(list1[0:2])
# Concatenate list
list2 = [1, 3, 'Ahmed', 'ali']

print(list2)
print(list1 + list2)

# lists in list
list3 = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 3, 5]
]
print(list3)
print(list3[0])
print(list3[0][0])

# functions add , remove , insert,  count(item), find item , len(), sort() pop(), index

animals = ['lion', 'fox', 'cow', 'lion']

animals.append('cat')
print(animals)

animals.remove('cat')
print(animals)

animals.insert(0, 'cat')
print(animals)

print(animals.count('lion'))
print(len(animals))

print('cat' in animals)

animals.sort(reverse=True)
print(animals)

# tuple

fruits = ('apple', 'banana', 'orange')
print(type(fruits))

print(len(fruits))

# set

set1 = {'ali', 'ali', 'salem'}
print(set1)

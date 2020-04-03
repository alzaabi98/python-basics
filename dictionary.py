# How to create dictionary
user = {
    'name': 'Abdulaziz',
    'email': 'alzaabi98@test.com',
    'password': 'sdfsdfsdfsdf'
}

print(type(user))

# How to acces item in dictionary via keys
print(user['password'])

# loop through keys using keys() function
for k in user.keys():
    print(k)

# loop through values using values() function
for v in user.values():
    print(v)

# loop through items using items() function
for k, v in user.items():
    print(k, v)

# How to add item in dictionay
user['age'] = 39
print(user)

# add  item using setDefault()

user.setdefault('city', 'Muscat')
print(user)
# get keys and store them in list

keysList = list(user.keys())
print(keysList)

# list of user - each user type is dictionary

users = [
    {
        'name': 'Abdulaziz',
        'email': 'alzaabi98@test.com',
    },
    {
        'name': 'Ahmed',
        'email': 'ahmed@test.com',
    },
    {
        'name': 'Ali',
        'email': 'ali@test.com',
    }

]

print(users)
print(users[2]['email'])

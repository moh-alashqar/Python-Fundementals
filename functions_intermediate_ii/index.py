# ----------------------------------------
# Update Values in Dictionaries and Lists
# ----------------------------------------
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] = 15
print(x)

# 2
students[0]['last_name'] = "Bryant"
print(students)

# 3
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

# 4
z[0]['y'] = 30
print(z)


# --------------------------------------
# Iterate Through a List of Dictionaries
# --------------------------------------
def iterateDictionary(some_list):
    for item in range(len(some_list)):
        count = 0
        for key, val in (some_list[item]).items():
            if count > 0:
                print(",", end = " ")
            count += 1
            print(key, "-", val, end = "")
        print("")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 


# --------------------------------------
# Get Values From a List of Dictionaries
# --------------------------------------
def iterateDictionary2(key_name, some_list): 
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# ---------------------------------------------
# Iterate Through a Dictionary with List Values
# ---------------------------------------------
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), end=" ")
        print(key.upper())
        for i in range(len(value)):
            print(value[i])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
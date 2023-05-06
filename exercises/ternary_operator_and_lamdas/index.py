# Ternary Operator
stacks = 2
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo')

# Lambdas 1
def map1(list, func):
    for i in range(len(list)):
        list[i] = func(list[i])
    return list

print(map1([1,2,3,4], lambda num: num * num))

print(6 ** 2) # Square

# Lambdas 2
some_list = [1, 2, 3, lambda num: num + 3]
print(some_list[3](3))

# Lambda 3 
def invoker(callback):
    print(callback(2))

invoker(lambda x: 2 * x)

# Lambda 4
add10 = lambda num: num + 10
print(add10(5))

# Lambda 5
my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a lambda as the first argument
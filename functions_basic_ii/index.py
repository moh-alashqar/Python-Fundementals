# Countdown
def countdown(num):
    num_list = []
    for i in range(num, -1, -1):
        num_list.append(i)
    return num_list
print(countdown(10))

# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([2,5]))

# First Plus Length
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,5,4,2,3]))

# Values Greater than Second
def second_greater_than(list):
    new_list = []
    if len(list) < 2: 
        return False
    else:
        for i in range(0, len(list)):
            if list[i] > list[1]:
                new_list.append(list[i])
        print(len(new_list))
        return new_list
print(second_greater_than([1]))
print(second_greater_than([1,5,4,3,8,7,9]))

# This Length, That Value
list = []
def length_and_value(length, value):
    for i in range(0, length):
        list.append(value)
    return list
print(length_and_value(4,8))
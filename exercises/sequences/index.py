my_list = [99, 4 ,2 ,5 ,-3]
my_tuple = (99, 4 ,2 ,5 ,-3)
my_str = "sequoia"
print(my_list[:])
print(my_tuple[1:])
print(my_str[:3])
print(my_tuple[2:4])
print(my_list, my_tuple, my_str)

print(max(my_list))
print(sum(my_list))
print(list(map(lambda x:x+1, my_list)))
print(min(my_list))
print(sorted(my_list))


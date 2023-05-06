# for loop
for x in range(0, 10, 1):
    print(x)

for x in range(0, 10):
    print(x)

for x in range(10):
    print(x)

for x in range(10, 0, -1):
    print(x)

my_list = [123, "ABC", "XYZ"]
for i in range(0, len(my_list)):
    print(my_list[i])

for i in my_list:
    print(i)

my_dic = {'name': 'Mohammed', 'age': '26'}
for x in my_dic:
    print(x)
    print(my_dic[x])

for key in my_dic.keys():
    print(key)

for value in my_dic.values():
    print(value)

for key, value in my_dic.items():
    print(key, "=", value)


# While loop
count = 0
while count < 5:
    print(count)
    count += 1

y = 0
while y > 5:
    print(y)
else:
    print("this is else")


# Loop Control
for val in "string":
    if val == "i":
        break
    print(val)

for cnt in "string":
    if cnt == "i":
        continue
    print(cnt)

    
y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1
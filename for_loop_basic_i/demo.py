# 1) Basic
for i in range(151):
    print(i)

# 2) Multiples of Five
for x in range(5, 1001):
    if x % 5 == 0:
        print(x)

# 3) Counting, the Dojo Way
for y in range(1, 101):
    if y % 5 == 0 and y % 10 != 0:
        print("Coding")
    elif y % 10 == 0:
        print("Coding Dojo")
    else: 
        print(y)

# 4) Whoa. That Sucker's Huge
sum = 0
for z in range(500001):
    if z % 2 != 0:
        sum += z
print(sum)

# 5) Countdown by Fours
for q in range(2018, 0, -4):
    print(q)

# 6) Flexible Counter
low_num = 2
high_num = 9
mult = 3
for k in range(low_num, high_num+1):
    if k % mult == 0:
        print(k)
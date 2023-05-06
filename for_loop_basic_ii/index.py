# Biggie Size
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie_size([-1,3,5,-5]))

# Count Positives
def count_positives(list):
    counter = 0
    for i in range(len(list)):
        if list[i] > 0:
            counter += 1
    list[len(list)-1] = counter
    return list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total
def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# Average
def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)
print(average([1,2,3,4]))

# Length
def length(list):
    return len(list)
print(length([37,2,1,-9]))
print(length([]))

# Minimum 
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0] 
        for i in range(len(list)):
            if list[i] < min:
                min = list[i]
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

# Maximum
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0] 
        for i in range(len(list)):
            if list[i] > max:
                max = list[i]
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

# Ultimate Analysis
def ultimate_analysis(list):
    min = list[0]
    max = list[0]
    sum_total = 0
    for i in range(len(list)):
        sum_total += list[i]
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    list_analysis = {'sum_total': sum_total, 'average': sum_total/len(list), 'minimum': min, 'maximum': max, 'length': len(list)}
    return list_analysis
print(ultimate_analysis([37,2,1,-9]))

# Reverse List
def reverse_list(list):
    for i in range(int(len(list)/2)):
        temp = list[0+i] 
        list[0+i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
print(reverse_list([37,2,1,-9]))
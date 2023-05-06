arr = [2,5,6,2,1,4,8,9,6,3,2,2,1,5,51,2,3,5,2]
def selection_sort(arr):
    for i in range(len(arr)):
        min = arr[i]
        min_index = i
        for j in range(i, len(arr)):
            if min > arr[j]:
                min = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(arr))
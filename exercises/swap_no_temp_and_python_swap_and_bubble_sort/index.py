# swap two params without a temp
def swap_params(a, b):
    a = a + b
    b = a - b
    a = a - b
    print ("a", a)
    print ("b", b)

swap_params(a=2,b=5)

# swap 2 array indexes in python
arr = [1,2,3,4]
arr[0], arr[1] = arr[1], arr[0]
print(arr)

# bubble sort
arr = [8,1,5,3,2,0]
def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubbleSort(arr))


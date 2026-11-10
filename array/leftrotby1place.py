def rotateArray(arr):
    n = len(arr)

    temp = arr[0]

    for i in range(1, n):
        arr[i - 1] = arr[i]

    arr[n - 1] = temp

    return arr
print(rotateArray([5,8,1,2]))

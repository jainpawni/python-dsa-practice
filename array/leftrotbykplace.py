def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def leftRotate1(arr, n, d):
    if n == 0:
        return arr

    d = d % n

    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)

    return arr



def leftRotate2(arr, d):
    n = len(arr)

    if n == 0:
        return arr

    d = d % n

    temp = arr[:d]

    for i in range(d, n):
        arr[i - d] = arr[i]

    for i in range(n - d, n):
        arr[i] = temp[i - (n - d)]

    return arr

print(leftRotate1([4,6,7,8,9],5,2),leftRotate2([4,6,7,8,9],2))

def rightRotate2(arr, d):
    n = len(arr)

    if n == 0:
        return arr

    d = d % n
    k=n-d

    temp = arr[:k]

    for i in range(k, n):
        arr[i - k] = arr[i]

    for i in range(n - k, n):
        arr[i] = temp[i - (n - k)]

    return arr
print(rightRotate2([1,2,3,4,5,6,7],3))

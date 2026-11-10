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


def rotate(self, nums, k):
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
       
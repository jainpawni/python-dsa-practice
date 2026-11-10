def unionArray(arr1, arr2):
    freq = {}

    for i in arr1:
        freq[i] = freq.get(i, 0) + 1

    for i in arr2:
        freq[i] = freq.get(i, 0) + 1

    return list(freq.keys())


def intersection1(arr1, arr2):
    freq = {}

    for i in arr1:
        freq[i] = freq.get(i, 0) + 1

    ans = []

    for i in arr2:
        if freq.get(i, 0) > 0:
            ans.append(i)
            freq[i] -= 1

    return ans

def intersection(arr1, arr2):
    freq = {}

    for i in arr1:
        freq[i] = freq.get(i, 0) + 1

    ans = []

    for i in arr2:
        if freq.get(i, 0) > 0:
            ans.append(i)
            freq[i] -= 1

    return ans
def moveZeros(n, arr):
    temp = []

    # Step 1: Store all non-zero elements
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    # Step 2: Copy non-zero elements back
    nz = len(temp)

    for i in range(nz):
        arr[i] = temp[i]

    # Step 3: Fill remaining positions with zero
    for i in range(nz, n):
        arr[i] = 0

    return arr





def moveZeros(n, arr):
    j = -1

    # Find the first zero
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    # If there are no zeros
    if j == -1:
        return arr

    # Move non-zero elements to the left
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr
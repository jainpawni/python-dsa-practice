def largestElement( nums):
    largest=nums[0]
    for i in range(len(nums)):
        if nums[i]>=largest:
            largest=nums[i]
    return largest
print(largestElement([4,6,9,3]))

def secondLargest(nums):
    nums = sorted(set(nums))

    if len(nums) < 2:
        return -1

    return nums[-2]
print(secondLargest([4,6,9,3]))

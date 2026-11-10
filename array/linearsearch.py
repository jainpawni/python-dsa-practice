def linearSearch(nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
print(linearSearch([3,6,8,5],6))
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maximum = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                count = 0

        return maximum
print(Solution().findMaxConsecutiveOnes([5,8,1,1,5,1,1,1,0]))
class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]
                

#or


    def twoSum2(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum2([2, 7, 11, 15], 22))
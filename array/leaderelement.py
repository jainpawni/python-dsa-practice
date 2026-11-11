class Solution:
 def leaders(self, nums):
    ans = []
    max_right = nums[-1]
    ans.append(max_right)

    for i in range(len(nums) - 2, -1, -1):   #or for i in range(-2, -len(nums)-1, -1):
            if nums[i] > max_right:
                 ans.append(nums[i])
                 max_right = nums[i]

    ans.reverse()
    return ans
print(Solution().leaders([16,17,4,3,5,2]))


class Solution:
    def rearrangeArray1(self, nums):
        ans = [0] * len(nums)

        pos = 0
        neg = 1

        for i in nums:
            if i > 0:
                ans[pos] = i
                pos += 2
            else:
                ans[neg] = i
                neg += 2

        return ans
#or

    def rearrangeArray2(self, nums):
        n = len(nums)
        ans = [0] * n

        pos, neg = 0, 1

        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2

        return ans
print(Solution().rearrangeArray1([3,1,-2,-5,2,-4]))
print(Solution().rearrangeArray2([3,1,-2,-5,2,-4]))
    
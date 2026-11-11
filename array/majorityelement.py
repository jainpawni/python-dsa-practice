class Solution(object):
    def majorityElement(self, nums):
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        max_freq = 0
        answer = 0

        for i in freq:
            if freq[i] > max_freq:
                max_freq = freq[i]
                answer = i

        return answer
    

#or-optimal,O(n) time, O(1) space,Boyer-Moore Voting Algorithm.


    def majorityElement(self, nums):
        count = 0
        candidate = None

        for i in nums:
            if count == 0:
                candidate = i

            if i == candidate:
                count += 1
            else:
                count -= 1

        return candidate
print(Solution().majorityElement([3,2,3]))

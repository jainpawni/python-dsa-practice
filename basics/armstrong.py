class Solution:
    def isArmstrong(self, n):
        original = n
        total = 0
        power = len(str(n))

        while n > 0:
            digit = n % 10
            total = total + digit ** power
            n = n // 10

        return total == original
print(Solution().isArmstrong(153))
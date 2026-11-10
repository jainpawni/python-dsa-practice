class Solution:
    def pattern9(self, n):
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end="")
            for k in range(2 * i + 1):
                print("*", end="")
            print()

        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for k in range(2 * (n - i) - 1):
                print("*", end="")
            print()
        
obj = Solution()
obj.pattern9(5)

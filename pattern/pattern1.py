class Solution:
    def pattern10(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
        for i in range(n,0,-1):
            for j in range(i-1):
                print("*",end="")
            print()
obj = Solution()
obj.pattern10(5)



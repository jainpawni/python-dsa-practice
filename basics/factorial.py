class Solution:
    def factorial(self,n):
        product=1
        for i in range(1,n+1):
            product= product*i
        return product
print(Solution().factorial(8))
        
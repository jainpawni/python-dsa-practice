class Solution:
    def primeUptoN(self, n):
        count = 0
        if n <= 1:
            return False

        for num in range(2, n + 1):
            prime = True
            #check every number from 1 to n to find which ones are prime.

            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break
 #checking each number separately. At the beginning, we assume the current number is prime. Then we check whether any number divides it evenly.
            if prime:
                count += 1

        return count
print(Solution().primeUptoN(67))
class Solution:
    def pattern12(self, n):
        for i in range(1, n + 1):

            # Left side: increasing numbers
            for j in range(1, i + 1):
                print(j, end="")

            # Spaces in the middle
            for j in range(1, 2 * (n - i) +1):
                print(" ", end="")

            # Right side: decreasing numbers
            for j in range(i, 0, -1):
                print(j, end="")

            print()
Solution().pattern12(5)

class Solution:
    def setZeroes(self, matrix):
        rows = set()
        cols = set()

        # First traversal: find original zeroes
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Second traversal: set corresponding cells to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return matrix
#GIVES NO.OF COL len(matrix[0])):
print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))


               
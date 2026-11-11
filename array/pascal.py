class Solution:
    def generate(self, numRows):
        ans = []

        for i in range(numRows):
            row = [1]

            if i > 0:
                for j in range(len(ans[i-1]) - 1):
                    row.append(ans[i-1][j] + ans[i-1][j+1])

                row.append(1)

            ans.append(row)

        return ans
    
    
    def getRow(self, rowIndex):
        row = [1]

        for i in range(rowIndex):
            newRow = [1]

            for j in range(len(row) - 1):
                newRow.append(row[j] + row[j+1])

            newRow.append(1)
            row = newRow

        return row
print(Solution().generate(5))
print(Solution().getRow(3))
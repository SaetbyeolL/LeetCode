# https://leetcode.com/problems/pascals-triangle/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an integer 'numRows', return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown.

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:      # 2-dimensional list(2D list)- row, column
        result = []                                           # list to store the results
        
        for currRow in range(numRows):                        # Set up a loop that iterates numRows times. i = current row
            row = []                                          # list to store the row
            
            for currColumn in range(currRow + 1):             # Set up a loop that iterates over the number of columns to be processed in the current row
                if currColumn == 0 or currColumn == currRow:  # when columns is the leftmost or rightmost row, append 1
                    row.append(1)     
                else:
                    row.append(result[currRow-1][currColumn-1]+result[currRow-1][currColumn]) # result[row][column]
            result.append(row)
        
        return result
                
        

# Test
sol = Solution()
numRows1 = 5
print(sol.generate(numRows1))
numRows2 = 1
print(sol.generate(numRows2))


























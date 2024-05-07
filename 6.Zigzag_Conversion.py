# https://leetcode.com/problems/zigzag-conversion/description/?envType=featured-list&envId=top-interview-questions%3FenvType%3Dfeatured-list&envId=top-interview-questions

# The "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAYPALISHIRING"
# Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = ""
        n = len(s)
        cycle_len = 2*numRows - 2                   # length of each cycle
        
        for i in range(numRows):
            for j in range(i, n, cycle_len):
                result += s[j]                      # Add first character of each row
                if 0 < i < numRows - 1:             # If not the first and last row
                    index = j + cycle_len - 2*i
                    if index < n:
                        result += s[index]
        
        return result

# Test
sol = Solution()
s1 = "PAYPALISHIRING"
numRows1 = 3
print(sol.convert(s1, numRows1))
s2 = "PAYPALISHIRING"
numRows2 = 4
print(sol.convert(s2, numRows2))
s3 = "A"
numRow3 = 1
print(sol.convert(s3, numRow3))



# https://leetcode.com/problems/plus-one/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# You are given a large integer represented as an integer array 'digits', where each 'digits[i]' is the 'i'번째 digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
        


# Solution: Time complexity: O(n), Memory complexity: O(1)
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> int:
        
        n = len(digits) # list length
        total = 0
        
        for i in range(n):     
            if digits[i] != 0: 
                digits[i] = (10** ((n-1)-i)) * digits[i] # multiply 10**n each elements
                total += digits[i]

        total += 1
        total_list = [int(j) for j in str(total)]
        
        return total_list
                
                
                
# Test code
sol = Solution()
digits1 = [1,2,3]
print(sol.plusOne(digits1))

digits2 = [4,3,2,1]
print(sol.plusOne(digits2))

digits3 = [9]
print(sol.plusOne(digits3))

digits4 = [9,9]
print(sol.plusOne(digits4))
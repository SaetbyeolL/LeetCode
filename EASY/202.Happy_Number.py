# https://leetcode.com/problems/happy-number/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1(where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not. 

class Solution:
    def isHappy(self, n: int) -> bool:
        number = set()
        
        while n != 1 and n not in number:
            number.add(n)
            result = 0
            
            for digit in str(n):
                result += int(digit)**2
            
            n = result
            
        return n == 1



# Test
sol = Solution()
n1 = 19
print(sol.isHappy(n1))
n2 = 2
print(sol.isHappy(n2))


















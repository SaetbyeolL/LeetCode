# https://leetcode.com/problems/sqrtx/?envType=featured-list&envId=top-interview-questions%3FenvType%3Dfeatured-list&envId=top-interview-questions

# Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

# class Solution:
#     def mySqrt(self, x: int) -> int:
        
        
        
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left, right = 0, x                     # Range for binary search
        result = 0                             # Variable to store the square root
        
        while left <= right:
            mid = left +  (right - left) // 2  # square of the midpoint, //: rounded down to the nearest whole number
            square = mid * mid
            
            if square == x:
                return mid                     # find the exact square root
            
            if square < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
            
            return result
            
            
    
# Test
# sol = Solution()
# x1 = 4
# print(sol.mySqrt(x1));

# sol = Solution()
# x2 = 8
# print(sol.mySqrt(x2));



























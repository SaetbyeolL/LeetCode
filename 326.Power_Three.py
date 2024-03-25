# https://leetcode.com/problems/power-of-three/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: 
            return False
    
        while n % 3 == 0:
            n /= 3
        
        return n == 1 

# Test
sol = Solution()
n1 = 27
print(sol.isPowerOfThree(n1))
n2 = 0
print(sol.isPowerOfThree(n2))
n3 = -1
print(sol.isPowerOfThree(n3))
n4 = 45 # 3 x 3 x 5
print(sol.isPowerOfThree(n4))














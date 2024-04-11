# https://leetcode.com/problems/number-of-1-bits/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Write a function that takes the binary representation of a positive integer 
# and returns the number of set bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            count += n & 1
            n >>= 1
            
        return count


# Test
solution = Solution()
print(solution.hammingWeight(11))  # Output: 3
print(solution.hammingWeight(128)) # Output: 1
print(solution.hammingWeight(2147483645)) # Output: 30
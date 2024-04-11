# https://leetcode.com/problems/reverse-bits/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Reverse bits of a given 32 bits unsigned integer.
# Note that in some languages, such as Java, there is no unsigned integer type. 
# In this case, both input and output will be given as a signed integer type. They should not affect your implementation, 
# as the integer's internal binary representation is the same, whether it is signed or unsigned.

# In Java, the compiler represents the signed integers using 2's complement notation. 
# Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

# solution 1
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


# solution 2
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        power = 31
        while n:
            result += (n & 1) << power
            n >>= 1
            power -= 1
        return result













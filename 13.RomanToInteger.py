# https://leetcode.com/problems/roman-to-integer/description/
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which si simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. The number four is written as IV.
# Because the one is before the five we subtract it making four. The same principle applies to the number 9, which is written as IX.


# Dictionary: O(n)
class Solution(object): 
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
class Solution(object):
    def romanToInt(self, s):
        RomanToIntMapping = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0; #Total result of converting Roman numerals to integers
        
        # loop Roman numeral from left to right
        for i in range(len(s)): # range: 0~(i-1)
            currentValue = RomanToIntMapping[s[i]] 
            if i == len(s) - 1: # if current index is last character of string,
                total += currentValue # all values add up
            else:
                if currentValue < RomanToIntMapping[s[i+1]]:
                    total -= currentValue
                else:
                    total += currentValue
        return total
                
            
sol = Solution();
print(sol.romanToInt("III")) #3
print(sol.romanToInt("XIV")) #14
print(sol.romanToInt("LVIII")) #58
print(sol.romanToInt("MCMXCIV")) #1994
            

        
# list : O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        RomanToIntMapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        listOfvalues = [] # list that store number
        for char in s:
            listOfvalues.append(RomanToIntMapping[char])
        total = 0
        
        for i in range(len(listOfvalues)):
            if i == len(listOfvalues) - 1 or listOfvalues[i] >= listOfvalues[i + 1]:
                total += listOfvalues[i]
            else:
                total -= listOfvalues[i]

        return total

solution = Solution()
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994


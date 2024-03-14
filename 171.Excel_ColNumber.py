# https://leetcode.com/problems/excel-sheet-column-number/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given a string 'columnTitle' that represents the column title as appears in an Excel sheet, return its corresponding column number.


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = {}
        title_length= len(columnTitle)
        total = 0
        
        for i in range(26):            
            alphabet[chr(65 + i)] = i + 1 
        
        for char in columnTitle:   
            if char in alphabet:
                total += alphabet[char] * 26**(title_length - 1)
                title_length -= 1
                
        return total
          
        
        

# Test
sol = Solution()
columnTitle1 = "A"
print(sol.titleToNumber(columnTitle1))
columnTitle1 = "AB"
print(sol.titleToNumber(columnTitle1))
columnTitle1 = "ZY"
print(sol.titleToNumber(columnTitle1))






















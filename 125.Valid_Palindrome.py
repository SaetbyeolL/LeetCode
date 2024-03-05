# https://leetcode.com/problems/valid-palindrome/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string 's', return 'true' if it is a palindrome, or 'false' otherwise.


# solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        lowercase = s.lower()
        processed_string = ''.join(filter(str.isalnum, lowercase))
        if not processed_string:
            return True

        return processed_string == processed_string[::-1]

# filter() : argument(function, iterable object) -> return list_type
# it creates a new iterable that returns only the elements for which the function provided as the first argument returns true 
# when applied to each element of the iterable received as the second argument
# function: Function used to evaluate each element
# iterable: A set of elements to be evaluated by a function

# ''.join() : connect each element of the list. it makes string


    
# solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()
        for i in lowercase:
            if i.isalnum() == False:
                lowercase = lowercase.replace(i,"")
        if lowercase == lowercase[::-1]:
            return True
        return False
                
        

# test
sol = Solution()
s1 = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s1))
s2 = "race a car"
print(sol.isPalindrome(s2))
s3 = " "
print(sol.isPalindrome(s3))



# list comprehension:
# result = []
# for i in range(10):
#     result.append(i * 2)

# result = [i * 2 for i in range(10)]

















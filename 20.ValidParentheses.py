# https://leetcode.com/problems/valid-parentheses/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given a string "s" containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


# stack v1
class Solution(object):
    def isValid(self, s):
        stack = []
        bracket = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }

        for char in s:
            if char in bracket.values():  
                stack.append(char)
            elif char in bracket.keys(): 
                if not stack or stack.pop() != bracket[char]:
                    return False
            else:
                return False  

        return not stack 

# ex) 
sol=Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("({[]})"))    # True


# stack v2
class Solution(object):
    def isValid(self, s):
        stack = [] # Initialize an empty stack to keep track of open brackets
        closeToOpen = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        
        for c in s:
            if c in closeToOpen: # If the current character is a closing bracket
                if stack and stack[-1] == closeToOpen[c]: # Check if the stack is not empty and clostToOpen[c] can be only ")}]"
                    stack.pop() # Remove the opening bracket from the stack since it is closed correctly
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False 


# ex) 
sol=Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("({[]})"))    # True
































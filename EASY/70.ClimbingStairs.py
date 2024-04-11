# https://leetcode.com/problems/climbing-stairs/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# You are climbing a staircase. It takes n steps to reach the top. 
# Each time you can either climb 1 or 2 steps, In how many distinct ways can you climb to the top?

# class Solution:
#     def climbStairs(self, n:int) -> int:


class Solution:
    def climbStairs(self, n:int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        previous = 1
        current = 2
        
        #step: previous - current - ways_to_current
        for _ in range(3, n+1): # _: dummy variable
            ways_to_current = previous + current # temporarily stores the number of ways to reach each staircase
            previous = current
            current = ways_to_current
        
        return current
    
    
# Test case
sol=Solution()
n1 = 5
n2 = 10
print(sol.climbStairs(n1))
print(sol.climbStairs(n2))




































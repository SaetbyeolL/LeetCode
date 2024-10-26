# https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
#1) hash map(dictionary) : O(n)
class Solution(object):
    def twoSum(self, nums, target):
        indices = {} #create dictionary
        
        for i, num in enumerate(nums): #
            diff = target - num
            if diff in indices: #check diff value is in hash map
                return [indices[diff], i] # return two numbers' index
            indices[num] = i #store current element and index in hash map
        
solution = Solution()    
nums = [2,7,11,15]            
twoSum = solution.twoSum(nums, 9)
print(twoSum)

# for index, value in enumerate(iterable):
#     # index: index of current element
#     # value: value of current element



#2) double-for loop : O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):  #check elements after i
                if nums[i] + nums[j] == target:
                    return [i, j]
                
solution = Solution()    
nums = [2,7,11,15]            
twoSum = solution.twoSum(nums, 9)
print(twoSum)



#3) set : O(n)
class Solution(object):
    def twoSum(self, nums, target):
        num_set = set() #create set()
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_set:
                return [nums.index(diff), i]
            num_set.add(i)

nums1 = [2, 7, 11, 15]
target1 = 9
sol = Solution()
result1 = sol.twoSum(nums1, target1)
print(result1)























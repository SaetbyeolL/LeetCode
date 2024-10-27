# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.


from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else :
                left += 1
        
            
sol = Solution()
numbers1 = [2,7,11,15]
target1 = 9
print(sol.twoSum(numbers1, target1))
numbers2 = [2,3,4]
target2 = 6
print(sol.twoSum(numbers2, target2))
numbers3 = [-1,0]
target3 = -1
print(sol.twoSum(numbers3, target3))

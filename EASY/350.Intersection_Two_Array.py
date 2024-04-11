# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

#Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

from typing import List
       
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        result = []

        if len(nums1) >= len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1
        
        for i in long:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1 
        # for i in long:   This for loop as same as above
        #     dic[i] = dic.get(i, 0) + 1
                
        for i in short:
            if i in dic and dic[i] > 0:
                result.append(i)
                dic[i] -= 1

        return result
        


# Test
sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersect(nums1,nums2))
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(sol.intersect(nums3,nums4))
nums5 = [1,2]
nums6 = [1,1]
print(sol.intersect(nums5,nums6))
nums7 = [2,1]
nums8 = [1,2]
print(sol.intersect(nums5,nums6))





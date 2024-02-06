# https://leetcode.com/problems/merge-sorted-array/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# You are given two integers arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, 
# nums1 has a length of m+n, where the first m elements denote the elements that should be merged, 
# and the last n elements are sent to 0 and should be ignored. nums2 has a length of n.



from typing import List
# class Solution:
#     def merge(self, nums1:List[int], m:int, nums2: List[int], n:int)-> None:
        

# solution 1: Slice assignment
class Solution:
    def merge(self, nums1:List[int], m:int, nums2: List[int], n:int)-> None:
        
        nums1[m:] = nums2[:n] # slice assignment : it alternates selected parts
        nums1.sort()
        nums2.clear()



# solution 2: for loop
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()



# solution3: 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # compares the two arrays starting from the back and inserts them sorted into nums1
        while m > 0 and n > 0: 
            if nums1[m-1] > nums2[n-1]:       # compares last elements of each array
                nums1[m+n-1] = nums1[m-1]     # insert nums1[m-1] into nums1[m+n-1]
                m -= 1                        # reduce index
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        # if there are elements in nums2 that have not been inserted, insert them
        while n > 0:
            nums1[n-1] = nums2[n-1] 
            n -= 1
        

# Test
# sol = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(sol.merge(nums1, m, nums2, n))

# num1 = [1]
# ms = 1
# num2 = []
# ns = 0
# print(sol.merge(num1, ms, num2, ns))

# numss1 = [0]
# mss = 0
# numss2 = [1]
# nss = 1
# print(sol.merge(numss1, mss, numss2, nss))









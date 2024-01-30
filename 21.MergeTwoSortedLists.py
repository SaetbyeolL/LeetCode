# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# You are given the heads of two sorted linked lists "lists1" and "lists2".
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


# 1) singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp = ListNode() # Create a empty node to start the merged list
        current = temp # Pointer to the current node in the merged list. This points to temp
        
        while list1 and list2:        # Check whether there are nodes in both that have not yet been checked(empty). if one of them is empty, it ends.
            if list1.val < list2.val: # Compare the values of the current nodes in both lists
                current.next = list1  # If the value in list1 is smaller, add it to the merged list
                list1 = list1.next    # Move to the next node in list1
            else:                     # If the value in list2 is smaller or equal, add it to the merged list
                current.next = list2 
                list2 = list2.next    # Move to the next node in list2
            
            current = current.next    # Move the current pointer in the merged list to the last added node
        
        # If one of them is not checked, add the remaining nodes to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return temp.next # Return the head of the merged list (skip the temp node)
    
# ex)
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution();
result = sol.mergeTwoLists(list1, list2)
# 결과 출력
while result:
    print(result.val, end=", ")
    result = result.next    
    
    
list1 = ListNode(1, ListNode(2, ListNode(4)))

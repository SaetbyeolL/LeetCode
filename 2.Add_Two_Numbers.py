# https://leetcode.com/problems/add-two-numbers/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: List[ListNode], l2: List[ListNode]) -> List[ListNode]:
        dummy_head = ListNode()     # Starting point of the resulting linked list
        current = dummy_head        # pointer to the current node
        carry = 0                   # Variable to store the round number
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            current_sum = val1 + val2 + carry
            carry = current_sum // 10
            current_digit = current_sum % 10
            
            current.next = ListNode(current_digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next
    
        
    
# Test
# l1 = [2,4,3], l2 = [5,6,4]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next















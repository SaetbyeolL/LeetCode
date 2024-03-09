# https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given the heads of two singly linked-lists 'headA' and 'headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        pointerA = headA
        pointerB = headB
        
        while pointerA != pointerB: # iterate until both pointers point to the same point
            pointerA = pointerA.next if pointerA else headB # When the pointer reaches the end, it moves to the beginning of the opposite list.
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA # returns the intersection point
        
        
        
        
        
        
        
        
        
        
    
        
# Test
sol = Solution()

intersected_node = ListNode(8)
intersected_node.next = ListNode(4)
intersected_node.next.next = ListNode(5)
listA = ListNode(4)
listA.next = ListNode(1)
listA.next.next = intersected_node
listB = ListNode(5)
listB.next = ListNode(6)
listB.next.next = ListNode(1)
listB.next.next.next = intersected_node
print(sol.getIntersectionNode(listA, listB))












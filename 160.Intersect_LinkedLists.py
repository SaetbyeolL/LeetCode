# https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given the heads of two singly linked-lists 'headA' and 'headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# solution1
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0                    # length of each linked list's node
        nodeA, nodeB = headA, headB          # first node
        
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
            
        nodeA, nodeB = headA, headB          # reset firstNode
        
        # Move the longer list forward by the difference in length between the two lists to align them at the same position
        while lenA > lenB:                   
            nodeA = nodeA.next
            lenA -= 1
        while lenB > lenA:
            nodeB = nodeB.next
            lenB -= 1
            
        while nodeA != nodeB:                # find intersection
            nodeA = nodeA.next
            nodeB = nodeB.next
            
        return nodeA              
    
    
# solution2   
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
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersected_node
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersected_node
print(sol.getIntersectionNode(headA, headB))












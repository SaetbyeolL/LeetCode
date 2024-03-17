# https://leetcode.com/problems/reverse-linked-list/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current_node = head                  # pointer: point to first node(ListNode(1))
        prev_node = None                     # pointer to previous node
        next_node = None                     # pointer to next node
        
        while current_node:                  # Repeat until current node becomes None
            next_node = current_node.next    # Temporarily store the next node
            current_node.next = prev_node    # Change the next node of the current node to the previous node
            prev_node = current_node         # Change previous node to current node
            current_node = next_node         # Change next node to current node
            
        return prev_node                     # Returning the previous node completes the linked list in reverse order




# Test
sol = Solution()
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
print(sol.reverseList(head1))

head2 = ListNode(1)
head2.next = ListNode(2)
print(sol.reverseList(head2))

head3 = ListNode()
print(sol.reverseList(head3))








# https://leetcode.com/problems/linked-list-cycle/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

# Given 'head', the head of a linked list, determine if the linked list has a cycle in it. 
# There is a cycle in a linked list if there is some node in the list that can be reached a gain by continuously following the 'next' pointer.
# Internally, 'pos' is used to denote the index of the node that tail's 'next' pointer is connected to. Note that 'pos' is not passed as a parameter.
# Return 'true' if there is a cycle in the linked list. Otherwirse, return 'false'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:          # linked list is empty or node is only 1(head = None or head.next = None)
            return False                       
        
        slow = head                            # it moves 1 node each time
        fast = head.next                       # it moves 2 nodes each time
        
        while slow != fast:                    # loop until slow and fast pointer meet. if it meets, we can notice there is cycle.
            if not fast or not fast.next:      # if fast = None or fast.next = None, we notice there is no cycle in linked list
                return False
            
            slow = slow.next                   # move next node
            fast = fast.next.next              # move next next node
        
        return True                            # when slow and fast match, it returns true
        

# test
sol = Solution()
head1 = [3, 2, 0, -4]                       # Regarding to requirement, head must receive a single ListNode object
                                            # connect each element in the list of head into a linked list to create a single ListNode object
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next
print(sol.hasCycle(head1))

head2 = [1,2]
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2
print(sol.hasCycle(head2))

head3 = [1]
head3 = ListNode(1)
head3.next = None
print(sol.hasCycle(head3))















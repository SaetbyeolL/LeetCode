# https://leetcode.com/problems/palindrome-linked-list/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

#Given the head of a singly linked list, return true if it is a palindrome or false otherwise. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        temp = head
        
        while temp:
            values.append(temp.val)
            temp = temp.next
        
        return values == values[::-1]
        


# Test
sol = Solution()
head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(sol.isPalindrome(head1))

head2 = ListNode(1, ListNode(2))
print(sol.isPalindrome(head2))

head3 = ListNode(1)
print(sol.isPalindrome(head3))




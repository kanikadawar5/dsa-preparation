# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = ListNode(0)
        temp.next = head
        
        prev = temp
        curr = head
        
        while curr and curr.next:
            first_node = curr
            second_node = curr.next
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev = first_node
            curr = first_node.next
        
        return temp.next

sol = Solution()
ll = ListNode([1, 2, 3, 4])
print(sol.swapPairs(ll))

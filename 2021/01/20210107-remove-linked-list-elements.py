"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        cnode = head  # current node
        while cnode:
            if cnode.val == val:
                if prev is None:
                    head = cnode.next
                else:
                    prev.next = cnode.next
            else:
                prev = cnode
            cnode = cnode.next
        return head

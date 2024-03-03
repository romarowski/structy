"""
#TODO
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    next = None
    cur = head
    while cur != None:
        next = cur.next
        cur.next = prev
        # update pointers
        prev = cur
        cur = next
    
    return prev

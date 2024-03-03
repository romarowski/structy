"""
2095. Delete the Middle Node of a Linked List

Medium

You are given the head of a linked list. Delete the middle node, and return the 
head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start 
using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or 
equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    cur = head
    n = 0
    while cur != None:
        cur = cur.next
        n+=1
    
    # handle the single element list 
    if n==1:
        return None

    middle = n // 2
    i = 0
    prev = None
    cur = head
    while True:
        if i == middle:
            prev.next = cur.next
            break
        prev = cur
        cur = cur.next
        i+=1
    
    return head
            
        

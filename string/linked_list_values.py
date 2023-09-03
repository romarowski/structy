import pdb 
class Node:
   def __init__(self, val):
     self.val = val
     self.next = None

def linked_list_values(head):
  l = []
  _append(head, l)
  return l
  
  
def _append(head, l):
  if head is None:
    pdb.set_trace()
    return l
  l.append(head.val)
  _append(head.next, l)  
  
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d  

print(linked_list_values(a))

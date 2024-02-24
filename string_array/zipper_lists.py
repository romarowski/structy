class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
  cur1 = head_1
  cur2 = head_2

  while (cur1 is not None) and (cur2 is not None):
    print(cur1.val, cur2.val)
   
    nxt1 = cur1.next
    nxt2 = cur2.next

    cur1.next = cur2
    cur2.next = nxt1

    cur1 = nxt1
    cur2 = nxt2
    print(cur1 is not None)
    print(cur2 is not None)
    ## cur1 = cur2
  
  print(cur1, cur2.val)


  return head_1



s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

zipper_lists(s, one)

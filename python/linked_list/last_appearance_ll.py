from collections import defaultdict
# List Node Class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lastAppearance(head):
    if not head or not head.next:
        return head
    dd = defaultdict(int)
    itr = head
    while itr:
        dd[itr.data]+=1
        itr = itr.next
    nh = nll = Node(-1)
    new_head = None
    itr = head
    while itr:
        if dd[itr.data] == 1:
            nll.next = Node(itr.data)
            nll = nll.next
        else:
            dd[itr.data]-=1
        itr = itr.next
    return nh.next


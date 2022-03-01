# Following is the class structure of the Node class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getListAfterDeleteOperation(head):
    # Write your code here.
    prev = head
    itr = head
    nh = cur = Node(itr.data)
    itr = itr.next
    while itr:
        if itr.data >= prev.data:
            cur.next = Node(itr.data)
            cur = cur.next
            prev = itr
        else:
            prev = itr
        itr = itr.next
    return nh

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def modularNode(head, k):
    #function should return the modular Node
    #if no such node is present then return -1
    itr = head
    lnode = None
    index = 0 
    while itr:
        index+=1
        if index % k == 0:
            lnode = itr
        itr = itr.next
    if lnode == None:
        return -1
    return lnode.data
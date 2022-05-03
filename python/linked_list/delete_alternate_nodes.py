class Solution: 
    def deleteAlt(self, head):
        itr = head
        tn = head
        itr = itr.next
        l = 1
        while itr:
            if l & 1 == 0:
                deln = tn.next
                tn.next = itr
                del deln
                tn = itr
            l+=1
            itr = itr.next
        if l&1 == 0:
            tn.next = None
        return head
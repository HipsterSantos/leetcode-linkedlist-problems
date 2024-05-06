class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def findNthNode(head,n):
    newHead = ListNode(0,head) # new head starts by adding before 0 and then the current list 
    first,second = newHead,newHead
    
    for _ in range(n+1):
        first = first.next
    while first is not None:
        first = first.next
        second = second.next

    #if we finish the first by reaching the end it means that we found the current node to remove
    #now we check it on second noe 
    second.next = second.next.next
    return newHead.next
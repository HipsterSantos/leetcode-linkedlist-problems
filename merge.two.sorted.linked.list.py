class ListNode:
    def __init__(self,val = 0 ,next = None):
        self.val = val
        self.next = next
        
def mergeTwoSortedList(list1:ListNode,list2:ListNode):
    dummy = ListNode(0)
    curr = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.vale: 
            curr.next = list1
        else: 
            curr.next = list2
        curr = curr.next
    curr.next = list1 if list1 is not None else list2
    return dummy.next

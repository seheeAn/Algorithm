# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        res = ListNode()
        tmp = res
        while n1 != None and n2 != None: # 둘 다 None이 아닐 때 까지
            if n1.val >= n2.val:
                tmp.next = ListNode(val=n2.val, next=None)
                tmp = tmp.next
                n2 = n2.next
            else:
                tmp.next = ListNode(val=n1.val, next=None)
                tmp = tmp.next
                n1 = n1.next
        
        if n1 == None:
            while n2 != None:
                tmp.next = ListNode(val=n2.val, next=None)
                tmp = tmp.next
                n2 = n2.next
        else:
            while n1 != None:
                tmp.next = ListNode(val=n1.val, next=None)
                tmp = tmp.next
                n1 = n1.next
    
        return res.next
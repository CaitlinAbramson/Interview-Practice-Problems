# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        node1 = l1
        node2 = l2
        
        ret = ListNode(None)
        current = ListNode(None)
        ret.next = current
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        while (node1 != None and node2 != None):
            if node1.val < node2.val:
                current.next = ListNode(node1.val)
                node1 = node1.next
                current = current.next
                
            else:
                current.next = ListNode(node2.val)
                node2 = node2.next
                current = current.next
          
        if node1 != None:
            current.next = node1
        
        if node2 != None:
            current.next = node2
        
        return ret.next.next
            
                
        
        
    
    
        
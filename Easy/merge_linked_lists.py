from leetcode_builtins import ListNode

def merge_linked_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
    new_list = ListNode()
    head = new_list
    
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            new_list.next = l1
            l1 = l1.next
        else:
            new_list.next = l2
            l2 = l2.next
        
        new_list = new_list.next
        new_list.next = None
    
    if l1 is None:
        new_list.next = l2
    if l2 is None:
        new_list.next = l1
    
    return head.next

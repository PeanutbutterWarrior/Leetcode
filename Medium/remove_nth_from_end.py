from leetcode_builtins import ListNode

def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
    if head.next is None:
        return None
    
    n_back = None
    length = 0
    body = head
    
    while body.next is not None:                
        length += 1
        
        if length > n:
            n_back = n_back.next
        elif length == n:
            n_back = head
        
        body = body.next
    
    try:
        n_back.next = n_back.next.next
    except AttributeError:
        # Removing first item
        return head.next
    
    return head

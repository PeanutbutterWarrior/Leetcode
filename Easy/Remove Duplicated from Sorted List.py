from leetcode_builtins import ListNode

def delete_duplicates(self, head: ListNode) -> ListNode:
    current_node = head
    previous = None
    while current_node is not None:
        if previous is not None and current_node.val == previous.val:
            previous.next = current_node.next
        else:
            previous = current_node
        current_node = current_node.next
    return head

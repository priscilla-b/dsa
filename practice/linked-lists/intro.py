
class ListNode:
    def __init__(self, data:0):
        self.data = data
        self.next = None


def list_to_linkedlist(lst:list) -> ListNode:
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head   # for moving the next pointer ahead to insert new nodes

    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next  # any updates to current updates head since they point to the same linked list
    
    return head


def count_nodes (head:ListNode) -> int:
    counter = 0
    while head:
        counter +=1
        head = head.next

    return counter


print(count_nodes(list_to_linkedlist([4, 2, 3, 10, 2])))
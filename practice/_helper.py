class Helper():
    def __init__(self):
        pass

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def list_to_linked_list(self, lst:list) -> ListNode:
        if not lst:
            return None
        
        head = self.ListNode(lst[0])
        current = head
        for val in lst[1:]:
            # since current is also pointing to head,
            # when current.next is updated, head.next is also updated
            # this is because a custom class like ListNode is mutable 
            # (same a lists and dictionaries). as a result  If you modify one reference 
            # to a mutable object, all references to that object see the change.
            current.next = self.ListNode(val)
            current = current.next
        return head
    
    def print_linked_list(self, node:ListNode):
        current = node
        values = []
        while current:
            values.append(current.val)
            current = current.next
        print(values)

    

        
        
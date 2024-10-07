# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        node = ListNode()
        current = node

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2.next = list2
            
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return node.next

     

def list_to_linked_list(lst:list) -> ListNode:
        if not lst:
            return None
        
        head = ListNode(lst[0])
        current = head
        for val in list[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

def print_linked_list(lst:ListNode):
    pass


solution = Solution()
list_to_linked_list([1, 2, 4])

# solution.merge_two_lists([1, 2, 4], [1, 3, 4])
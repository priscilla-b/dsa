# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def delete_duplicates(self, head:ListNode) -> ListNode:
        # traverse linkedlist and remove duplicate values
        current = head

        while current and current.next:
            # if the current value is the same as the next one, skip the next node
            if current.val == current.next.val:
                # skip next node by updating it to next node after it
                current.next = current.next.next
            else:
                current = current.next

            
        return head
        
       



def list_to_linkedlist(lst:list) -> ListNode:
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


head = list_to_linkedlist([1, 1, 2])

solution = Solution()
solution.delete_duplicates(head)


# https://leetcode.com/problems/remove-duplicates-from-sorted-list
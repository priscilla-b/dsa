from _helper import Helper

ListNode = Helper.ListNode


class Solution:
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        
        # using a dummy node to handle cases where the head node itself might 
        # need to be removed
        dummy = ListNode()
        dummy.next = head
        head = dummy
        current = head

        while current and current.next:
            # easier to check the next node so that i can skip it by 
            # setting it to its next 
            if current.next.val == val:
               current.next = current.next.next
            else:       
                current = current.next

        # returning head.next to avoid including the dummy node in the result
        return head.next
        







helper = Helper()

lst = helper.list_to_linked_list([6, 2, 6, 3, 4, 5, 6])

solution = Solution()

reversed_ = solution.remove_elements(lst, 6)

print(helper.print_linked_list(reversed_))
from _helper import Helper


ListNode = Helper.ListNode


class Solution:

    def deleteDuplicates(self, head:ListNode) -> ListNode:
        set_ = set()
        current = head
        output = ListNode()

        while current:
            val = current.val
            if val not in set_:
                set_.add(val)
                output.next = current
                
            current = current.next

        return output.next

            


    # def deleteDuplicates(self, head: ListNode) -> ListNode:

    #     # keeping a dummy node to cater for instances where the head itself 
    #     # might need to be deleted  
    #     dummy = ListNode()
    #     dummy.next = head  # Link dummy node to head to begin tracking

    #     current = head
    #     # storing the previous node so that i can use it if current node needs to be removed
    #     prev = dummy  


    #     while current and current.next:
    #         if current.val == current.next.val:
    #             # since both are duplicates remove current and current.next 
    #             # by skipping the current and its next node
    #             current = current.next.next
    #             prev.next = current  # reset prev.next to current to also skip the duplicates in prev
    #         else:
    #             prev = current
    #             current = current.next
               

        
    #     return dummy.next



helper = Helper()
head = helper.list_to_linked_list([1, 2, 3, 3, 4, 4, 5])

solution = Solution()
answer = solution.deleteDuplicates(head)
helper.print_linked_list(answer)


     
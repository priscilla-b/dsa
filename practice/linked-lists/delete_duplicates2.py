from _helper import Helper


ListNode = Helper.ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # keeping a dummy node to cater for instances where the head itself 
        # might need to be deleted  
        dummy = ListNode()

        current = head

        # storing the previous node so that i can use it if current node needs to be removed
        prev = dummy  


        while current and current.next:
            if current.val == current.next.val:
                # since both are duplicates remove current and current.next 
                # by setting it to previous node
                current = current.next
                prev.next = current.next
            else:
                prev = current

            current = current.next
               

        
        return head



helper = Helper()
head = helper.list_to_linked_list([1, 2, 3, 3, 4, 4, 5])

solution = Solution()
answer = solution.deleteDuplicates(head)
helper.print_linked_list(answer)


     
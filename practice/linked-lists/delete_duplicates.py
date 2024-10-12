from _helper import Helper

ListNode = Helper.ListNode

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
        
       



helper = Helper()


head = helper.list_to_linkedlist([1, 1, 2])

solution = Solution()
solution.delete_duplicates(head)


# https://leetcode.com/problems/remove-duplicates-from-sorted-list
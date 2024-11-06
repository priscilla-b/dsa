from _helper import Helper

ListNode = Helper.ListNode

class Solution:
    def middle_node(self, head: ListNode) -> ListNode:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        


    





helper = Helper()
head = helper.list_to_linked_list([1, 2, 3, 4, 5, 6])


solution = Solution()
helper.print_linked_list((solution.middle_node(head)))







    
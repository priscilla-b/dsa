from _helper import Helper

ListNode = Helper.ListNode

class Solution:
    # very unoptimized solution. idea is there, but execution wasn't great
    def is_palindrome_n(self, head:ListNode) -> bool:
        node_count = self.get_node_count(head)

        # if head has only one node, it's a palindrome
        if node_count == 1:
            return True

        mid = node_count // 2

        current = head

        half_stack = []

        position = 1
        while current:
            # traverse the list and store half of it's node in a stack
            # traverse the other half by comparing each val with the item at the
            # top of the stack. If they're equal throughout, then it's a palindrome list
            
             # if node_count is odd, skip middle node
            if position == mid+1 and (node_count % 2 != 0):
                current = current.next

            if position <= mid:
                half_stack.append(current.val)
            else:         
                if current.val != half_stack.pop():
                    return False
                
           
            
            current = current.next
            position += 1
        
        return True

    def is_palindrome(self, head:ListNode) -> bool:
        # instead of counting nodes to find the midpoint
        # use a slow and fast pointer.
        # move fast pointer at twice the speed of the slow pointer
        # such that by the time the fast pointer gets to the end,
        # the slow pointer will be in the middle

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # once fast is at the end, slow is at mid point
        # so reverse second half of list
        second_half = self.reverse_list(slow)

        # The slow pointer identifies the start of the second half of the list.
        # Reversing the second half of the list will not modify the first half directly.
        # However, after the reversal, the last node of the first half will no longer
        # be connected to the second half due to the reversal, effectively splitting
        # the list into two parts.
        first_half = head
        # compare first half with reversed current half
        while second_half:
            if first_half.val != second_half.val:
                return False
            
            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverse_list(self, node:ListNode) -> ListNode:
        current = node
        prev = None
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_

        return prev
                



    def get_node_count(self, head:ListNode) -> int:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        return count


    





helper = Helper()
head = helper.list_to_linked_list([1,2,2,1])


solution = Solution()
print(solution.get_node_count(head))
print(solution.is_palindrome(head))






    
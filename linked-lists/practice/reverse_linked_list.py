from _helper import Helper


ListNode = Helper.ListNode

class Solution:

    # less optimal approach. creates a new node with current node value and inserts 
    # start of output node
    def reverse_list_n(self, head: ListNode) -> ListNode:
        current = head   # for advancing the head (original list) to the next pointer
        output = None  # for storing final answer (reversed list) that will be returned

        while current:
            new_node = ListNode(current.val)
            # this will insert the new node to the start of the output linked list
            
            # place the new node at the beginning of the output node
            # this will start the reversal
            new_node.next = output

            # set the output node as the new node for the next iteration
            output = new_node

            current = current.next

        return output
    
    # more optimal approach. reverses the node in place
    def reverse_list_opt(self, head:ListNode) -> ListNode:
        current = head
        prev = None
        
        while current:
            next_ = current.next

            current.next = prev

            prev = current

            current = next_

        return prev
           

helper = Helper()

lst = helper.list_to_linked_list([1, 2, 3])

solution = Solution()

reversed_ = solution.reverse_list_opt(lst)

print(helper.print_linked_list(reversed_))




# https://leetcode.com/problems/reverse-linked-list
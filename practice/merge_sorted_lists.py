# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # since both lists are already sorted,
        # you can merge them directly in the order the 
        # items appear in the list
        node = ListNode()  # dummy listnode to build the merged list
        current = node  # used to traverse and build the merged list


        # for when both the first and second list have values
        while list1 and list2:
            # merge the lists by placing the lesser value together
            # to be able to sort in place
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        # when there are some remaining values in the first list,
        # append it to the end of the merged lsit
        if list1:
            current.next = list1

         # when there are some remaining values in the second list,
        # append it to the end of the merged lsit
        if list2:
            current.next = list2

        # returning node.next instead of node to avoid including the first variable
        # that was added (0) when the dummy node was created
        return node.next

     
# not needed in leetcode
def list_to_linked_list(lst:list) -> ListNode:
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        # since current is also pointing to head,
        # when current.next is updated, head.next is also updated
        # this is because a custom class like ListNode is mutable 
        # (same a lists and dictionaries). as a result  If you modify one reference 
        # to a mutable object, all references to that object see the change.
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list for debugging
def print_linked_list(node):
    current = node
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(values)


list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])


solution = Solution()
merged_list = solution.merge_two_lists(list1, list2)
print_linked_list(merged_list)




# https://leetcode.com/problems/merge-two-sorted-lists/
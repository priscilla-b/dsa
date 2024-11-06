from _helper import Helper

ListNode = Helper.ListNode

class Solution:
    # brute-force solution. 
    # keep a track of all the nodes, traverse through the linked list and check
    # if a node exists in the list of visited nodes
    # has a space complexity of O(n)
    def hasCycle_n(self, head: ListNode) -> bool:
        node_list = []
        
        current = head

        while current and current.next:

            if current in node_list:
                return True
            
            node_list.append(current)
            
            current = current.next

        return False
    
    # optimized solution using tortoise and hare algorithm (Floyd's cycle detection algorithm)
    # has O(1) space complexity
    def hasCycle_opt(self, head: ListNode) -> bool:
        """
        The idea of this algorithm is that, if there's no cycle, then the hare (the fast pointer)
        will eventually reach the end of the linked list (return None).
        However since the hare moves faster than the tortoise (the slow pointer) if there's a cycle, 
        the hare will eventually lap the tortoise (i.e. slow == fast)
        """
        # If the list is empty or has only one element, no cycle can exist
        if not head or not head.next:
            return False
        
        # Initialize two pointers, slow and fast
        slow = head
        fast = head.next
        
        # Move slow pointer one step and fast pointer two steps at a time
        while slow != fast:
            # If fast or fast.next is None, it means we've reached the end and there's no cycle
            if not fast or not fast.next:
                return False
            
            slow = slow.next          
            fast = fast.next.next    
        
        # If slow == fast, a cycle exists
        return True

       
        

        

def create_linked_list_cycle(lst:ListNode, pos: int):
    current = lst
    node_at_pos = ListNode(None)
    curr_pos = 0
    while current.next != None:
        if curr_pos == pos:
            node_at_pos = current

        curr_pos += 1
        current = current.next
      
    current.next = node_at_pos




helper = Helper()
lst = helper.list_to_linked_list([3, 2, 0, -4])
lst_cycle = create_linked_list_cycle(lst, 1)
solution = Solution()
print(solution.hasCycle_opt(lst))


















# https://leetcode.com/problems/linked-list-cycle/description
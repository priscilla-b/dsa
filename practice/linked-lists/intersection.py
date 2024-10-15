from _helper import Helper

ListNode = Helper.ListNode

class Solution:
    # hashing approach: does not optimize space
    def get_intersection_node_n(self, headA: ListNode, headB: ListNode) -> ListNode:

        currentA = headA
        currentB = headB

        # keep a set of visited nodes in the first head
        nodesA = set()

        while currentA:
            nodesA.add(currentA)
            currentA = currentA.next
        
        # check if any node in B is equal to any of the visited nodes in A
        while currentB:
            if currentB in nodesA:
                return currentB

            currentB = currentB.next


        return None


    # two-pointer approach: optimizes both space and time
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        # traverse both lists at the same time with a pointer for each
        # if one pointer gets to the end of its lists, point it to the other
        # this forces the pointers to traverse the same number of nodes
        # as a result, they meet the intersection at the same time 
        # or reach their ends at the same time
            
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            pointerA = headB if not pointerA else pointerA.next
            pointerB = headA if not pointerB else pointerB.next

        return pointerA

            



# not part of leetcode solution
def create_intersected_linkedlist(
        listA:list, listB:list, skipA:int, skipB:int, intersectVal:int) -> list[ListNode]:
    
    headA = ListNode()
    headB = ListNode()
    currentA = headA
    currentB = headB

    intersectNode = ListNode(intersectVal)

    create_intersect_head(currentA, listA, skipA, intersectNode)

    create_intersect_head(currentB, listB, skipB, intersectNode)

    return [headA.next, headB.next]

def create_intersect_head(
        current:ListNode, lst:list, skip:int, intersectNode:ListNode):
    
    position = 0
    for val in lst:
        if position == skip:
            current.next = intersectNode
        else:
            current.next = ListNode(val)
        current = current.next

        position += 1


helper = Helper()
# lsts = create_intersected_linkedlist([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3, 8)
lsts = create_intersected_linkedlist([1, 9, 1, 2, 4], [3, 2, 4], 3, 1, 2)
helper.print_linked_list(lsts[0])
helper.print_linked_list(lsts[1])

solution = Solution()
node = solution.get_intersection_node(lsts[0], lsts[1])
helper.print_linked_list(node)





    
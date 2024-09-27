# Linked Lists

With linked lists, items can be anywhere in memory since they don't need to be stored next to each other like in arrays.
Each item stores the address of the next item in the list, linking the memory addresses together.

Adding an item to a linked list is faster compared to arrays since the new items can be stored anywhere, so memory does not have to be reallocated when list size increases. For example, if you add an item to the middle of a linked list, you just have to change the address the previous item points to. Same logic works for deletes.

The disadvantage with linked list is that it's slower to access a single item, since you don't know it's exact position in the list. You have to go through each item in the linked list to get the one you're looking for (sequential access).

Linked lists have a constant insertion time (O(1)) but a linear reading time (O(n))

A work around the slowness of random access of linked lists and the slowness of insertion of arrays is to have a combined data structure (an array of linked lists). Each element in an array will contain a linked list, making it easier to search within linked lists, and faster to insert in arrays.

## Implementation with Python

A linked list consits of nodes, and each node has two elements: the data and the pointer to the next node.
![linked-list](linked_list.png)
[source](https://www.geeksforgeeks.org/python-linked-list/)

```py

# creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # initialize an empty linked list by setting the head as none

    # insertion at beginning of node
    def insert_at_start(self, data):
        new_node = Node(data)  # create a new node with the given data
        if self.head is None:  
            # set the new node as the head if the linked list is empty(head is none)
            self.head = new_node
            return
        else:
            # if the node has a head then set the existing head as the next item 
            # and set the new node as the new head of the linked list
            new_node.next = self.head
            self.head = new_node

    # insert node at a given index
    def insert_at_index(self, data, index):
        if (index == 0):
            self.insert_at_start(data)
            return

        # since index > 0, we have to traverse the entire linked list
        # to find the node at the position we want to insert
        current_node = self.head
        current_position = 0  # we can only start from the head, so using 0 as current position

        while (current_position < index):
            # if we're not yet at the index position, then move to the next node
            # and increment the current position by 1 to reflect the movement to the next node
            current_node = current_node.next
            current_position += 1

            if current_node == None:
                # we're at the end of the linked list, so that index is 
                # not present in the linked list
                print('index not present')
                return


        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
        return
    

linked_list = LinkedList()
linked_list.insert_at_start(12)
linked_list.insert_at_start(15)
linked_list.insert_at_start(18)
linked_list.insert_at_index(20, 1)
```

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
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
```

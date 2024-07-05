## Linked Lists

With linked lists, items can be anywhere in memory since they don't need to be stored next to each other like in arrays.
Each item stores the address of the next item in the list, linking the memory addresses together.

Adding an item to a linked list is faster compared to arrays since the new items can be stored anywhere, so memory does not have to be reallocated when list size increases. For example, if you add an item to the middle of a linked list, you just have to change the address the previous item points to. Same logic works for deletes.

The disadvantage with linked list is that it's slower to access a single item, since you don't know it's exact position in the list. You have to go through each item in the linked list to get the one you're looking for (sequential access).

Linked lists have a constant insertion time (O(1)) but a linear reading time (O(n))
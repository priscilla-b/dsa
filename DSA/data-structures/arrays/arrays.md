## Arrays

Arrays store elements contiguously(next to each other) in memory.

Adding a new item to an array can be slow because memory might have to be reallocated to accommodate the increase in size of the array. A good workaround is to pre-allocate memory for the expected final size of the array, but that might just be a waste of memory if the pre-allocated space is not used up.
There's also a chance that the computer might run out of memory to store a list if the size is really large.

If you want to insert an element in the middle of an array for example, you'd have to change the position of all the elements that will come after it to reflect the increase in size of the array. Same logic works for deletes.

However, because you know the position(index) of each item in an array, it's easy to access items directly (random access), without having to go through each element one at a time like with linked lists. Because of this property of arrays, they are used more compared to linked lists.

Arrays have a constant reading time (O(1)), but a linear insertion time (O(n)).

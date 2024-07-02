## Binary Search
Binary search is an algorithm that takes a sorted list of elements as its input and returns the position of the element being searched for or `null` if that element does not exist in the list.

For example, if given a list with about 100 elements and you're looking for an element, a simple search will go through each item in the list and confirm one at a time if that's the element being searched. This can take about 100 steps if the item being searched for is in the last position. 

For a binary search, instead of going through each item one by one, you start from the middle position, and then go to the next middle position, until the exact item position is found. So with 100 elements start from 50, then 25, then 13, then 7, then 4, 2, and 1. This takes 7 steps for the 100 elements in the worst case scenario. The same approach will be used for any number of elements.

The mathematical model is this: for any list of length `n`, a binary search will take `log2n` steps to run in the worst case, whereas a simple search will take `n` steps.
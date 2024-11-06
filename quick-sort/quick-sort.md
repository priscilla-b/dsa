## Quick Sort

Faster than selection sort and used more frequently in real life. 

Also uses D&C.
The base case of an a quick sort algorithm is an empty array or an array with one element since you can just return those values without performing any "sort"
```py
if len(arr) < 2:
    return arr
```

If the array has two elements, it can be easily sorted by checking if first element is smaller than second, and swapping them if it isn't.

In general, the quick sort algorithm follows this process:
- first pick a pivot (an element from the array to start with)
- partition the array into two sub-arrays: one with elements less than the pivot and one with elements greater than the pivot
- call quicksort recursively on the two sub-arrays
- join the sorted arrays and the pivot together to get your final sorted array

For example, given an array `[33, 15, 10]`. If the pivot is `33`, then the array of elements less than `33` is `[15, 10]` and the array of elements greater than `33` is `[]`. As a result the final array will be computed as `quick_sort([15, 10]) + 33 + quick_sort([])`

Same logic can be applied for an array of any number of elements.

The speed of the quick sort algorithm depends on the pivot chosen.
It has a Big O runtime of `O(n log n)` on average but can get to an `O(n^2)` runtime in the worst case.
If you pick the first item as the pivot, and the array is already sorted, you're going to recursively iterate through an array with more elements, and so you'll have a longer call stack. Compared to picking say the middle element as the pivot, the array is split into two and so you'll have a shorter call stack.

Quick sort will complete in O(n log n) time on average if you choose a random element in the array as the pivot
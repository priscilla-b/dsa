## Big O Notation

When evaluating the time complexity of algorithms, instead of just looking at the runtimes for the initial input size, also consider runtimes when the input size grows. For example, when you compare an `O(n)` runtime to an `O(log n)` runtime, when input size increases, the algorithm with the `O(n)` runtime will also increase in time complexity at the same rate, but the algorithm with the `O(log n)` complexity gets even much faster.

Algorithm speed isn’t measured in seconds, but in growth of the number of operations.

Big O notation always considers the worst case scenario.
Some Big O runtimes:
- O(log n) : log time
- O(n): linear time
- O(n * log n): e.g. a fast sorting algorithm like quicksort
- O(n^2): exponential time. e.g. a slow sorting algorithm like selection sort
- O(n!):  e.g: a really slow algorithm, like the traveling salesperson


** the complexity of an algorithm is not measured by if the algorithm contains a loop or not,
but by how the operations grow as input size grows. e.g. `for i in range(n) ... ` has an O(n) complexity because the operation grows by size of n as n grows. `for i in range(100)` will have an O(1) complexity because the input size is fixed.

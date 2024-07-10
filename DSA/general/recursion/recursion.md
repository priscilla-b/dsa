## Recursion

A recursive function is a function that calls itself. 

Every recursive function has two parts: the base case and the recursive case.
**The base case** is the stage or condition with which the function should exit. for example, when counting down from a number(n) to 1, the result should not go below 1, so the function should exit when `n <= 1`.
**The recursive case** is the stage where the function calls itself, so more like a repeat of the logic.
For example, in the countdown example, the function will call itself whenever it wants to print the next number in the countdown sequence.

```py
def countdown(n):
    print i
    if i <= 1:  # base case
        return
    else:
        countdown(i-1) # recursive case
```

### The call stack
**A stack** is a data structure that allows you to add an item to its top(push) and remove an item from the same top (pop). Operates on a last in first out (LIFO) principle.

Your computer uses a call stack to store functions and their variables in memory whenever a function call is made. the most recent function call is allocated to the top of the memory stack. 

When function calls are being returned, the function at the topmost point of the stack gets returned first, which means the function that was most recently called (the inner function) gets returned first and the order follows until the first function that was called (outer function) gets returned.

*In other words, when you call a function from another function, the calling function is paused in a partially completed state.*


### The call stack with recursion
Recursive functions use the call stack as a way to iterate through items or function calls to perform repeatable operations instead of having a dedicated array of items like loops(for, while) need.
While this is convenient, there's also a cost associated with saving numerous function calls in memory at a time.
If your call stack is too long, you might have to rewrite your code to use loops *tail recursion* (not supported by all languages)



## Divide and Conquer (D & C)
Recursive algorithm. Generally useful for solving problems where a clear, straight-forward solution does not look possible.
According to D&C, with every recursive call, you have to reduce your problem.

Strategy:
- first figure out the base case -> the simplest possible case
- divide or decrease your problem until it becomes the base case

For example, if you want to divide a rectangular piece of land into square plots of the same size, you can first start by figuring out the largest square of land you can use as a plot (base case).
You can now divide your plot of land to ensure that all the plots meet the meet case.

D&C is not a simple algorithm that you can apply to all problems, but rather a way to think about a problem

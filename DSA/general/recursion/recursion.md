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

### The stack
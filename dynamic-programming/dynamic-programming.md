# Dynamic Programming

Involves solving complex problems by breaking them into smaller, subproblems and then solving those ones first.

When solving dynamic programming problems, you usually have some constraint and a set of options you want to select to maximize that constraint (like the set-covering problem).
Unlike approximation algorithms like the greedy algorithm that usually provides an approximate value, dynamic programming solutions can provide an exact value to these problems.

The solutions to subproblems are usually stored in a tabular form ***(memoization)*** and reused in other sub-problems to find the final optimal solution.
Usually finding the optimal solution for a subproblem involves:
- checking for the previous optimal value
- checking for current optimal value + any residual value
- picking the maximum(or minimum) of these two
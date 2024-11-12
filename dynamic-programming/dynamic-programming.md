# Dynamic Programming

Involves solving complex problems by breaking them into smaller, subproblems and then solving those ones first.

When solving dynamic programming problems, you usually have some constraint and a set of options you want to select to maximize that constraint (like the set-covering or knapsack problem).
Unlike approximation algorithms like the greedy algorithm that usually provides an approximate value, dynamic programming solutions can provide an exact value to these problems.

The solutions to subproblems are usually stored in a tabular form ***(memoization)*** and reused in other sub-problems to find the final optimal solution.
Usually finding the optimal solution for a subproblem involves:
- checking for the previous optimal value
- checking for current optimal value + any residual value
- picking the maximum(or minimum) of these two

## General tips for dynamic programming solutions
- Every dynamic programming solution involves a grid
- The values in the cells of the grid are usually the values you're trying to optimize, like the value of goods in the knapsack problem
- Each cell is a subproblem, so think about how you can divide your problem into subproblems. That helps identify the axes for the grid. For example, in the knapsack problem, the x axis of the grid has the possible weights of the knapsack from the smallest unit to the largest, while the y axis has the items you want to put in the knapsack. 
- There's no single formula for calculating a dynamic programming solution. You just need to use these guidelines and figure out how to break your problem into smaller subproblems

## More Applications

### Longest common substring

For finding how closely related two strings are by checking which continuous set of characters those strings have in common. For example, doing fuzzy word lookups in dictionaries and other databases.
E.g. given two words, "fish" and "hish" the longest common substring between them is "ish".

To use dynamic programming to solve this problem, you can put each character in the two strings as the x and y axis to form a grid. Each cell in the grid will represent a character from each string. 

For each cell, check if the two characters are equal. If they are, the value in the cell is incremented by taking the value of the top-left cell relative to the current cell and adding 1.

Keep track of the maximum value in the grid, as that will represent the length of the longest common substring.
This will usually be value at the most-bottom-right cell in the grid.

### Longest common sequence
Instead of checking for the longest continuous characters common to two strings, you can also just check the number of characters in the sequence (string) that the two words have in common.
Finds the longest sequence of characters that appear in both strings in the same order, but not necessarily consecutively. For example, between "fish" and "fosh," the longest common subsequence is "fsh."

To solve this with dynamic programming:
- put each character in the two strings as the x and y axis to form a grid. Each cell in the grid will represent a character from each string. 
- for each cell, check if the the two characters match
- if they do, set the value of the cell as the value of the relative top-left cell + 1
- if they don't set the value of the cell as the max of the value of the cell directly above it or the value of the cell to the left. The max value represents the longest subsequence found so far until that point
The value in the bottom-right cell of the grid represents the length of the longest common subsequence.


### When to Use Longest common sequence vs. Longest common substring
Use Longest Common Substring when you need a continuous sequence of matching characters. This is often used in problems requiring exact matching of patterns or phrases, like DNA matching or exact string comparison.

Use Longest Common Subsequence when you're interested in a pattern of characters that appear in both strings in the same order, but don't need to be contiguous. This is useful for problems like version control, diff tools, or finding the similarity between sequences or documents where characters might appear non-consecutively but still reflect shared structure.


## Practical Applications
- Used by biologists for finding similarities in DNA strands
- Used in version control systems to differences between two files
- Used for *Levenshtein distance* calculations, which measure how similar two strings are. This is used for things like spell-check or checking if a user is uploading copyrighted databases
- Used for implementing word-wrapping functionalities. Helps to figure out where to wrap so that the length stays consistent
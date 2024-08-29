# Breadth-first Search

An algorithm that runs on graph data structures to find the shortest distance between two points.
It helps answer two types of questions:

1. Is there a path from Node A to Node B?
2. What is the shortest path from Node A to Node B?

## Use cases

- write a checkers algorithm that calculates the fewest moves to victory
- write a spell checker
- find the doctor (or anything else) closest to you in your network


In breadth-first search, nodes or connections closest to the starting point are preferred to those farther away, so search starts (intuitively) from nodes closest to the start point.

The algorithm uses a `queue` data structure to store the order in which items can be searched.

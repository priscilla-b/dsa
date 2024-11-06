# Breadth-first Search

An algorithm that runs on graph data structures to find the shortest distance between two points.
It helps answer two types of questions:

1. Is there a path from Node A to Node B?
2. What is the shortest path from Node A to Node B?

## Use cases

- write a checkers algorithm that calculates the fewest moves to victory
- write a spell checker
- find the doctor (or anything else) closest to you in your network


In breadth-first search, nodes or connections closest to the starting point are preferred to those farther away, so search starts (intuitively) from nodes closest to the start point. That's how breadth-first search finds the shortest paths between two nodes.

## Queues
The algorithm uses a `queue` data structure to store the items to be searched.
Items that are added to the queue first are searched first in that order.
Queue is a FIFO (First In, First ) data structure, compared to Stacks that are LIFO (Last In, First Out)

You cannot access random elements in the queue.
There are only two operations with queues:
- Enqueue: add an item to the queue
- Dequeue: remove an item from the queue

## Implementation
Implementing breadth-first search involves traversing each node in your graph (following each edge from one node to another). Running time for this is O(number of edges)

It also involves keeping a queue of items to be searched. Adding an item to a queue take O(1) time, so adding n items to a queue takes O(n) time

Combined time complexity is therefore O(number of vertices(items) + number of edges) = O(V+E)

Process:
1. Keep a queue containing items to be searched
2. Pop an item off the queue
3. Check if the item meets the search criteria and exit
4. If it doesn't add all the neighbors(dependents) of that item item to the queue
5. Repeat from step 2 until queue is empty
6. If queue is empty there are no search results

Additionally keep a list of searched items to track what if an item has been searched already before searching it again to avoid running into a possible infinite loop

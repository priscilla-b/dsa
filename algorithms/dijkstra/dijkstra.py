
"""
- You need three hash tables:
    - one for the graph
    - one for the costs (how long it takes to get to each node from the start)
    - one for the parents of each node

- You also need an array to keep track of all the nodes that are already processed 
to avoid processing the same node more than once
"""

graph = {}

# store the weight of each node edge as the value of the hash map
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


# using infinity to represent nodes whose costs are not known yet
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parent of a node is the node it was reached from
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

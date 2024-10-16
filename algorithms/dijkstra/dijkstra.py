
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

print(graph)
print(costs)
print(parents)


def find_lowest_cost_node(node):
    # get the cost and neighbors of that node
    cost = costs[node]
    neighbors = graph[node]

    # calculate the new cost of each neighbor by adding the current cost
    # of the parent node to its edge weight
    for n in neighbors.key():
        new_cost = cost + neighbors[n]

        # if the new cost is smaller than its original cost
        # you found a shorter path to the node, so update the costs hash table

        if new_cost < costs[n]:
            costs[n] = new_cost

        # since we found a new path to node n through the current node, 
        # update the parent of node n as the current node
        parents[n] = node

    # once the costs for all the neighbors of the node has been updated,
    # mark the node as processed
    processed.append(node)